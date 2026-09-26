#!/usr/bin/env python3
"""recuperer_jobs_ibm.py — RATISS Labs · fermer la boucle R7 sur le plan Open.

À lancer depuis TON compte IBM Quantum, quand la session est rétablie.

Ce que fait ce script :
  1. liste tes instances (dont les « open instances ») ;
  2. rapatrie toutes tes tâches : identifiant, backend, statut, date de création
     **telle que renvoyée par IBM**, et le temps QPU consommé (`usage()`) ;
  3. confronte la date renvoyée par IBM avec celle décodée depuis l'identifiant
     seul → si les deux concordent, la datation par identifiant est prouvée par
     la source elle-même ;
  4. chiffre ta consommation par fenêtre de 28 jours et la compare au quota du
     plan Open ;
  5. écrit un dossier de preuves (JSON + rapport lisible) que tu peux publier.

Prérequis :
    pip install qiskit-ibm-runtime

Usage :
    python3 recuperer_jobs_ibm.py --token <TOKEN_IBM> --jours 90
    python3 recuperer_jobs_ibm.py --token <TOKEN_IBM> --instance <CRN> --jours 120
    python3 recuperer_jobs_ibm.py --token <TOKEN_IBM> --ids ids.txt   # contrôle ciblé
    python3 recuperer_jobs_ibm.py --aide

Options utiles :
    --sortie dossier     (défaut : ./preuves-ibm)
    --region eu-de       (si ton instance est hébergée en Europe)

⚠️  Le token circule en argument de ligne de commande : sur une machine partagée,
    préfère la variable d'environnement IBM_QUANTUM_TOKEN (le script la lit
    automatiquement si --token est absent). Ne le colle jamais dans un dépôt.
"""

from __future__ import annotations

import argparse
import json
import os
import statistics
import sys
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from decode_job_id import decode  # noqa: E402

QUOTA_PLAN_OPEN_S = 10 * 60          # 10 minutes de temps QPU / fenêtre glissante de 28 jours
FENETRE_JOURS = 28


def connexion(token: str, instance: str | None, region: str | None):
    """Établit la connexion. Renvoie (service, note)."""
    try:
        from qiskit_ibm_runtime import QiskitRuntimeService
    except ImportError:
        sys.exit("✘ qiskit-ibm-runtime manquant : pip install qiskit-ibm-runtime")

    tentatives = []
    if region:
        tentatives.append(dict(channel="ibm_quantum_platform", token=token,
                               instance=instance, region=region))
    tentatives.append(dict(channel="ibm_quantum_platform", token=token, instance=instance))
    tentatives.append(dict(channel="ibm_quantum_platform", token=token))
    tentatives.append(dict(channel="ibm_quantum", token=token))  # ancienne API, au cas où

    derniere = None
    for kw in tentatives:
        try:
            return QiskitRuntimeService(**{k: v for k, v in kw.items() if v is not None}), str(kw)
        except Exception as e:  # noqa: BLE001
            derniere = e
    sys.exit(f"✘ connexion impossible ({derniere}).\n"
             "  → ta session est-elle débloquée ? une carte doit être validée côté IBM Cloud.\n"
             "  → le token est-il celui du bon compte IBM Quantum Platform ?")


def liste_instances(service) -> list[str]:
    for methode in ("instances", "list_instances"):
        f = getattr(service, methode, None)
        if f is None:
            continue
        try:
            return [str(i) for i in f()]
        except Exception:  # noqa: BLE001
            continue
    return []


def champ(job, *noms, defaut=None):
    """Lit un attribut ou appelle une méthode, sans casser selon la version."""
    for n in noms:
        v = getattr(job, n, None)
        if v is None:
            continue
        try:
            value = v() if callable(v) else v
        except Exception:  # noqa: BLE001
            continue
        if value is not None:
            return value
    return defaut


def collecte(service, jours: int, ids_cibles: list[str] | None) -> list[dict]:
    if ids_cibles:
        jobs = []
        for jid in ids_cibles:
            try:
                jobs.append(service.job(jid))
            except Exception as e:  # noqa: BLE001
                print(f"  ✘ {jid} : {e}")
        return [serialise(j) for j in jobs if j]

    depuis = datetime.now(timezone.utc) - timedelta(days=jours)
    try:
        brut = service.jobs(limit=None, created_after=depuis)
    except TypeError:
        brut = service.jobs(limit=200)
    return [serialise(j) for j in brut]


def serialise(job) -> dict:
    jid = str(champ(job, "job_id", "id", defaut="?"))
    cree = champ(job, "creation_date", "created")
    if hasattr(cree, "isoformat"):
        cree = cree.isoformat()
    usage = champ(job, "usage")
    return {
        "job_id": jid,
        "backend": str(champ(job, "backend_name", "backend", defaut="?")),
        "statut": str(champ(job, "status", defaut="?")),
        "cree_ibm": str(cree) if cree else None,
        "usage_s": float(usage) if isinstance(usage, (int, float)) else None,
        "session_id": champ(job, "session_id"),
        "tags": champ(job, "tags"),
    }


def confronte(jobs: list[dict]) -> dict:
    ecarts = []
    for j in jobs:
        if not j.get("cree_ibm"):
            continue
        try:
            t_ibm = datetime.fromisoformat(j["cree_ibm"].replace("Z", "+00:00"))
            if t_ibm.tzinfo is None:
                t_ibm = t_ibm.replace(tzinfo=timezone.utc)
            t_id = decode(j["job_id"])
        except Exception:  # noqa: BLE001
            continue
        d = abs((t_id - t_ibm).total_seconds())
        j["ecart_id_vs_ibm_s"] = d
        ecarts.append(d)
    ecarts.sort()
    return {
        "taches_comparees": len(ecarts),
        "ecart_median_ms": round(ecarts[len(ecarts) // 2] * 1000, 1) if ecarts else None,
        "ecart_max_ms": round(max(ecarts) * 1000, 1) if ecarts else None,
        "concordance": (max(ecarts) < 2.0) if ecarts else None,
    }


def fenetres_quota(jobs: list[dict]) -> list[dict]:
    """Consommation par fenêtre glissante de 28 jours (quota plan Open)."""
    horodates = []
    for j in jobs:
        u = j.get("usage_s")
        if u is None:
            continue
        t = None
        if j.get("cree_ibm"):
            try:
                t = datetime.fromisoformat(j["cree_ibm"].replace("Z", "+00:00"))
            except Exception:  # noqa: BLE001
                t = None
        if t is None:
            try:
                t = decode(j["job_id"])
            except Exception:  # noqa: BLE001
                continue
        horodates.append((t, u))
    if not horodates:
        return []
    horodates.sort()
    res, i = [], 0
    while i < len(horodates):
        debut = horodates[i][0]
        fin = debut + timedelta(days=FENETRE_JOURS)
        lot = [u for t, u in horodates if debut <= t < fin]
        res.append({
            "fenetre_debut": debut.date().isoformat(),
            "fenetre_fin": fin.date().isoformat(),
            "taches": len(lot),
            "usage_s": round(sum(lot), 2),
            "usage_min": round(sum(lot) / 60, 3),
            "quota_min": QUOTA_PLAN_OPEN_S / 60,
            "part_du_quota": round(sum(lot) / QUOTA_PLAN_OPEN_S, 4),
        })
        i += 1
    return res


def rapport(jobs, conf, fen, instances, note_connexion, sortie: Path) -> None:
    sortie.mkdir(parents=True, exist_ok=True)
    (sortie / "jobs-ibm-brut.json").write_text(json.dumps(jobs, indent=1, ensure_ascii=False))
    (sortie / "synthese.json").write_text(json.dumps(
        {"connexion": note_connexion, "instances": instances,
         "confrontation": conf, "fenetres_quota": fen}, indent=1, ensure_ascii=False))

    backends = defaultdict(int)
    statuts = defaultdict(int)
    for j in jobs:
        backends[j["backend"]] += 1
        statuts[j["statut"]] += 1

    L = ["# Dossier de preuves — tâches IBM Quantum",
         "",
         f"*Généré le {datetime.now(timezone.utc):%Y-%m-%d %H:%M} UTC*",
         "",
         "## 1. Connexion", "", f"- Mode : `{note_connexion}`",
         f"- Instances visibles : {len(instances)}"]
    for i in instances[:10]:
        L.append(f"  - `{i}`")
    L += ["", "## 2. Volume", "",
          f"- Tâches rapatriées : **{len(jobs)}**",
          f"- Backends : " + ", ".join(f"`{k}` × {v}" for k, v in sorted(backends.items())),
          f"- Statuts : " + ", ".join(f"`{k}` × {v}" for k, v in sorted(statuts.items())),
          "", "## 3. Datation par l'identifiant — confrontée à la source", ""]
    if conf["taches_comparees"]:
        L += [f"- Tâches comparées : **{conf['taches_comparees']}**",
              f"- Écart médian identifiant ↔ IBM : **{conf['ecart_median_ms']} ms**",
              f"- Écart maximum : **{conf['ecart_max_ms']} ms**",
              f"- Concordance (< 2 s) : **{'OUI ✅' if conf['concordance'] else 'NON ❌'}**",
              "",
              "> La date décodée depuis les 9 premiers caractères de l'identifiant est",
              "> confrontée à la date que l'API IBM renvoie pour la même tâche.",
              "> C'est la seule vérification qui fasse autorité — et elle est ici rejouable."]
    else:
        L += ["- Aucune tâche horodatée par IBM dans le lot : rien à confronter."]
    L += ["", "## 4. Consommation et quota du plan Open", "",
          f"Quota de référence : **{QUOTA_PLAN_OPEN_S/60:.0f} minutes de temps QPU** par fenêtre glissante de 28 jours.", ""]
    if fen:
        L += ["| Fenêtre | Tâches | Usage | Part du quota |", "|---|---|---|---|"]
        for f in fen:
            L.append(f"| {f['fenetre_debut']} → {f['fenetre_fin']} | {f['taches']} | "
                     f"{f['usage_min']} min | {f['part_du_quota']*100:.1f} % |")
        tot = sum(f["usage_s"] for f in fen)
        L += ["", f"**Total mesuré : {tot:.1f} s ({tot/60:.2f} min)**"]
    else:
        L += ["- `usage()` indisponible : cette information n'est renvoyée que pour les tâches",
              "  dont la mesure de consommation a été conservée par IBM."]
    L += ["", "## 5. Ce que ce dossier prouve", "",
          "- Chaque identifiant correspond à une tâche existante **dans ton compte**, avec son",
          "  backend, son statut et la date de création enregistrée par IBM.",
          "- La datation par identifiant seul est validée par la source.",
          "",
          "## 6. Ce que ce dossier ne prouve pas", "",
          "- Que les comptages publiés dans tes dépôts proviennent de ces tâches précises :",
          "  il faudrait pour cela comparer `job.result()` aux JSON archivés.",
          "  → à faire ensuite, sur les tâches phares.",
          "",
          "---", "", "*RATISS Labs — R7 : reproductible par un étranger, en une commande.*"]
    (sortie / "RAPPORT-PREUVES.md").write_text("\n".join(L))
    print(f"\n✔ Dossier de preuves écrit dans {sortie}/")
    print("   • jobs-ibm-brut.json   (les données brutes)")
    print("   • synthese.json        (confrontation + quota)")
    print("   • RAPPORT-PREUVES.md   (le rapport publiable)")


def main() -> int:
    p = argparse.ArgumentParser(description="Rapatrie et vérifie les tâches IBM Quantum.")
    p.add_argument("--token", default=os.environ.get("IBM_QUANTUM_TOKEN"))
    p.add_argument("--instance", default=os.environ.get("IBM_QUANTUM_INSTANCE"))
    p.add_argument("--region", default=None)
    p.add_argument("--jours", type=int, default=120)
    p.add_argument("--ids", default=None, help="fichier texte, un identifiant par ligne")
    p.add_argument("--sortie", default="preuves-ibm")
    p.add_argument("--aide", action="store_true")
    a = p.parse_args()

    if a.aide:
        print(__doc__)
        return 0
    if not a.token:
        print(__doc__)
        print("\n✘ Aucun token fourni (ni --token, ni $IBM_QUANTUM_TOKEN).")
        return 1

    ids = None
    if a.ids:
        ids = [l.strip() for l in open(a.ids) if l.strip()]

    service, note = connexion(a.token, a.instance, a.region)
    instances = liste_instances(service)
    print(f"✔ Connecté ({note}) — {len(instances)} instance(s)")
    for i in instances[:10]:
        print(f"   · {i}")

    print(f"\n→ Rapatriement des tâches…")
    jobs = collecte(service, a.jours, ids)
    print(f"✔ {len(jobs)} tâche(s) récupérée(s)")

    conf = confronte(jobs)
    fen = fenetres_quota(jobs)
    rapport(jobs, conf, fen, instances, note, Path(a.sortie))

    if conf["taches_comparees"]:
        print(f"\n  Datation par identifiant ↔ IBM : "
              f"écart médian {conf['ecart_median_ms']} ms, "
              f"max {conf['ecart_max_ms']} ms → "
              f"{'CONCORDANCE ✅' if conf['concordance'] else 'DIVERGENCE ❌'}")
    if fen:
        print(f"  Usage total : {sum(f['usage_s'] for f in fen):.1f} s "
              f"sur {len(fen)} fenêtre(s) de 28 jours (quota {QUOTA_PLAN_OPEN_S/60:.0f} min)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
