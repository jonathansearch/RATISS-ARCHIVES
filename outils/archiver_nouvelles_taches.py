#!/usr/bin/env python3
"""archiver_nouvelles_taches.py — RATISS Labs · ne plus jamais perdre une tâche.

Problème constaté le 26/09/2026 : les 57 dépôts contiennent 86 identifiants de
tâches, mais les campagnes les plus récentes n'y figurent pas. Les preuves
n'existaient que dans le compte IBM — donc nulle part.

Ce script archive **au format exact déjà utilisé dans les dépôts** :

    jobs_ibm/<identifiant>.json
    {"job", "test", "backend", "created_utc", "status", "n_pubs", "counts", "recup"}

…plus un journal daté (`JOURNAL-TACHES.md`) qui trace la croissance :
c'est lui qui permettra, dans trois mois, de réconcilier un compteur affiché
par IBM avec ce qui est réellement archivé.

Usage :
    # tout ce qui n'est pas encore archivé, sur 120 jours
    python3 archiver_nouvelles_taches.py --token <TOKEN> --depots /chemin/aux/depots

    # depuis une date précise, dans un seul dépôt
    python3 archiver_nouvelles_taches.py --token <TOKEN> --depots ~/RATISS-QVM --depuis 2026-09-23

    # ce qui a été soumis depuis moins de 2 jours (à lancer après chaque session)
    python3 archiver_nouvelles_taches.py --token <TOKEN> --depots ~/RATISS-QVM --jours 2

    # simulation : montre ce qui serait archivé, sans rien écrire
    python3 archiver_nouvelles_taches.py --token <TOKEN> --depots . --simulation

⚠️  Le token ne doit jamais être écrit dans un fichier versionné.
    Préférer : export IBM_QUANTUM_TOKEN=...  puis lancer sans --token.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from decode_job_id import decode  # noqa: E402
from recuperer_jobs_ibm import champ, connexion, liste_instances, serialise  # noqa: E402


# --- extraction des comptages, robuste aux versions de primitives -------------
def _compte_depuis(valeur):
    """Best-effort : transforme une valeur de résultat en {bitstring: entier}."""
    if valeur is None:
        return None
    if hasattr(valeur, "get_counts"):                      # BitArray, Counts, QuasiDistribution
        try:
            c = valeur.get_counts()
            if isinstance(c, dict):
                return {str(k): int(v) for k, v in c.items()}
        except Exception:  # noqa: BLE001
            pass
    if isinstance(valeur, dict):
        if valeur and all(isinstance(v, (int, float)) for v in valeur.values()) \
           and all(isinstance(k, str) and set(k) <= {"0", "1"} for k in valeur):
            return {str(k): int(v) for k, v in valeur.items()}
        # DataBin / dict imbriqué : on descend
        for v in valeur.values():
            r = _compte_depuis(v)
            if r:
                return r
    if hasattr(valeur, "data"):                            # PubResult
        return _compte_depuis(valeur.data)
    try:                                                   # tableau de bitstrings
        import numpy as np
        if isinstance(valeur, np.ndarray):
            vals = valeur.ravel().tolist()
            if vals and all(isinstance(x, str) for x in vals):
                out = {}
                for s in vals:
                    out[str(s)] = out.get(str(s), 0) + 1
                return out
    except Exception:  # noqa: BLE001
        pass
    return None


def extraire_comptages(job) -> tuple[list[dict], int]:
    """Renvoie (liste des comptages par publication, nombre de publications vues)."""
    try:
        res = job.result()
    except Exception as e:  # noqa: BLE001
        return [], 0
    comptages, vus = [], 0
    try:
        pubs = list(res)
    except TypeError:
        pubs = [res]
    for pub in pubs:
        vus += 1
        c = None
        data = getattr(pub, "data", pub)
        try:
            for nom in getattr(data, "keys", lambda: [])():
                c = _compte_depuis(getattr(data, nom))
                if c:
                    break
        except Exception:  # noqa: BLE001
            pass
        if not c:
            c = _compte_depuis(data)
        if c:
            comptages.append(c)
    return comptages, vus


# --- archivage ----------------------------------------------------------------
def dossier_jobs(depot: Path) -> Path:
    for cand in (depot / "jobs_ibm", depot / "passerelle_quantique" / "jobs_ibm",
                 depot / "resultats" / "jobs_ibm"):
        if cand.exists():
            return cand
    return depot / "jobs_ibm"


def deja_archivees(depot: Path) -> set[str]:
    d = dossier_jobs(depot)
    if not d.exists():
        return set()
    return {p.stem for p in d.glob("*.json")}


def archive(job, cible: Path, libelle: str, simulation: bool) -> dict:
    infos = serialise(job)
    comptages, vus = ([], 0) if simulation else extraire_comptages(job)
    cree = None
    try:
        cree = decode(infos["job_id"]).isoformat()
    except Exception:  # noqa: BLE001
        cree = infos.get("cree_ibm")
    charge = {
        "job": infos["job_id"],
        "test": libelle,
        "backend": infos["backend"],
        "created_utc": cree or infos.get("cree_ibm"),
        "status": infos["statut"],
        "n_pubs": len(comptages) if comptages else (vus or 0),
        "counts": comptages,
        "recup": "ok" if comptages else "metadata-seulement",
        "usage_s": infos.get("usage_s"),
        "cree_ibm": infos.get("cree_ibm"),
        "session_id": infos.get("session_id"),
    }
    if not simulation:
        cible.write_text(json.dumps(charge, indent=1, ensure_ascii=False))
    return charge


def journal(depot: Path, charges: list[dict], simulation: bool) -> None:
    """Tient un journal daté — c'est lui qui trace la croissance dans le temps."""
    if not charges or simulation:
        return
    p = depot / "JOURNAL-TACHES.md"
    ancien = p.read_text() if p.exists() else "# Journal des tâches IBM Quantum\n\n*Une ligne par tâche archivée. Ce journal est la mémoire du volume.*\n\n| archivé le | tâche | soumise le | backend | statut | publications |\n|---|---|---|---|---|---|\n"
    lignes = []
    for c in charges:
        lignes.append(f"| {datetime.now(timezone.utc):%Y-%m-%d %H:%M} | `{c['job']}` | "
                      f"{(c.get('created_utc') or '')[:16]} | {c['backend']} | {c['status']} | {c['n_pubs']} |")
    p.write_text(ancien.rstrip("\n") + "\n" + "\n".join(lignes) + "\n")


def main() -> int:
    ap = argparse.ArgumentParser(description="Archive les tâches IBM non encore conservées.")
    ap.add_argument("--token", default=os.environ.get("IBM_QUANTUM_TOKEN"))
    ap.add_argument("--instance", default=os.environ.get("IBM_QUANTUM_INSTANCE"))
    ap.add_argument("--region", default=None)
    ap.add_argument("--depots", default=".", help="dépôt (ou dossier parent de dépôts)")
    ap.add_argument("--test", default="campagne courante", help="libellé enregistré dans le champ test")
    ap.add_argument("--jours", type=int, default=None, help="ne prendre que les N derniers jours")
    ap.add_argument("--depuis", default=None, help="date ISO : ne prendre qu'après")
    ap.add_argument("--simulation", action="store_true")
    ap.add_argument("--aide", action="store_true")
    a = ap.parse_args()

    if a.aide:
        print(__doc__); return 0
    if not a.token:
        print(__doc__); print("\n✘ Aucun token (--token ou $IBM_QUANTUM_TOKEN)."); return 1

    racine = Path(a.depots).expanduser().resolve()
    depots = [racine] if (racine / ".git").exists() else [d for d in racine.iterdir() if d.is_dir()]
    connus: set[str] = set()
    for d in depots:
        connus |= deja_archivees(d)
    print(f"→ {len(depots)} dépôt(s) · {len(connus)} tâche(s) déjà archivée(s)")

    service, note = connexion(a.token, a.instance, a.region)
    print(f"✔ Connecté ({note}) · {len(liste_instances(service))} instance(s)")

    depuis = None
    if a.depuis:
        depuis = datetime.fromisoformat(a.depuis).replace(tzinfo=timezone.utc)
    elif a.jours:
        depuis = datetime.now(timezone.utc) - timedelta(days=a.jours)

    try:
        brut = service.jobs(limit=None, created_after=depuis) if depuis else service.jobs(limit=None)
    except TypeError:
        brut = service.jobs(limit=200)

    inconnues = [j for j in brut if str(champ(j, "job_id", "id", defaut="?")) not in connus]
    print(f"→ {len(inconnues)} tâche(s) non archivée(s) à traiter"
          f"{' (simulation)' if a.simulation else ''}")

    cible = dossier_jobs(depots[0]); cible.mkdir(parents=True, exist_ok=True)
    charges = []
    for i, job in enumerate(inconnues, 1):
        try:
            c = archive(job, cible / f"{champ(job,'job_id','id')}.json", a.test, a.simulation)
            charges.append(c)
            print(f"  [{i}/{len(inconnues)}] {c['job']}  {c['backend']:14s} {c['status']:10s} "
                  f"{c['n_pubs']} pubs  recup={c['recup']}")
        except Exception as e:  # noqa: BLE001
            print(f"  [{i}/{len(inconnues)}] ✘ {e}")
    journal(depots[0], charges, a.simulation)

    r = sum(1 for c in charges if c["recup"] == "ok")
    print(f"\n✔ {len(charges)} tâche(s) traitée(s) · {r} avec comptages complets")
    if len(charges) - r:
        print(f"  ⚠️ {len(charges)-r} en « metadata-seulement » : les comptages n'ont pas pu être")
        print("     extraits automatiquement. Télécharge l'export `job-<id>.zip` depuis la")
        print("     plateforme et utilise comparer_export_ibm.py pour reconstituer la charge.")
    if not a.simulation:
        print(f"  → fichiers écrits dans {cible}")
        print(f"  → journal : {depots[0] / 'JOURNAL-TACHES.md'}")
        print("\n  Pense à committer tout de suite : une tâche non poussée est une tâche perdue.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
