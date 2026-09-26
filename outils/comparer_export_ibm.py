#!/usr/bin/env python3
"""comparer_export_ibm.py — RATISS Labs · fermer le dernier maillon de R7.

IBM Quantum exporte les résultats d'une tâche dans une archive nommée
``job-<identifiant>.zip`` (c'est de là que vient le fichier
``job-dap8jg8pqrnc739b0hc0.zip``). Ce script compare, publication par
publication, les comptages de l'export IBM avec les comptages archivés dans
le dépôt.

C'est LA vérification qui manquait : non pas « la tâche existe », mais
« les chiffres publiés sont bien ceux qu'IBM a renvoyés pour cette tâche ».

Usage :
    # une tâche
    python3 comparer_export_ibm.py --export job-dap8jg8pqrnc739b0hc0.zip \\
        --archive ratiss-focal/passerelle_quantique/jobs_ibm/dap8jg8pqrnc739b0hc0.json

    # un lot : toutes les archives d'un dossier
    python3 comparer_export_ibm.py --exports-dir telechargements/ \\
        --archives-dir ratiss-focal/passerelle_quantique/jobs_ibm/

    # rapport JSON
    python3 comparer_export_ibm.py --exports-dir dl/ --archives-dir arch/ --json verdict.json

Sortie : code 0 si tout concorde, 1 sinon (utilisable dans une CI).

Aucune dépendance : zipfile + json de la bibliothèque standard.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import zipfile
from pathlib import Path

ID_RE = re.compile(r"(?:job[-_])?([a-z0-9]{20})")


def _compte_dict(o) -> bool:
    """Vrai si ``o`` ressemble à un dictionnaire de comptages {bitstring: entier}."""
    if not isinstance(o, dict) or not o:
        return False
    cles = list(o.keys())
    if not all(isinstance(k, str) for k in cles):
        return False
    if not all(isinstance(v, int) for v in o.values()):
        return False
    if not all(set(k) <= {"0", "1"} for k in cles):
        return False
    return len({len(k) for k in cles}) == 1  # même largeur de registre


def extraire_comptages(o, out: list | None = None) -> list[dict]:
    """Parcourt une structure JSON et renvoie les comptages dans l'ordre rencontré."""
    if out is None:
        out = []
    if isinstance(o, dict):
        if _compte_dict(o):
            out.append(o)
        else:
            for v in o.values():
                extraire_comptages(v, out)
    elif isinstance(o, list):
        for v in o:
            extraire_comptages(v, out)
    return out


def lire_export(chemin: Path) -> tuple[str | None, list[dict]]:
    """Renvoie (identifiant deviné, comptages) depuis un .zip, un .json ou un dossier."""
    comptages: list[dict] = []
    jid = None
    fichiers: list[Path] = []
    if chemin.is_dir():
        fichiers = [p for p in chemin.rglob("*") if p.suffix in (".json", ".zip")]
    else:
        fichiers = [chemin]

    for p in fichiers:
        if p.suffix == ".zip":
            with zipfile.ZipFile(p) as z:
                for nom in z.namelist():
                    if nom.endswith(".json"):
                        try:
                            comptages += extraire_comptages(json.loads(z.read(nom)))
                        except Exception:  # noqa: BLE001
                            pass
            m = ID_RE.search(p.stem)
            if m and not jid:
                jid = m.group(1)
        else:
            try:
                comptages += extraire_comptages(json.loads(p.read_text(errors="ignore")))
                m = ID_RE.search(p.stem)
                if m and not jid:
                    jid = m.group(1)
            except Exception:  # noqa: BLE001
                pass
    return jid, comptages


def comparer(archive: dict, comptages_ibm: list[dict]) -> dict:
    """Compare les comptages d'un export aux comptages archivés d'une charge brute."""
    attendus = archive.get("counts") or []
    if not isinstance(attendus, list):
        attendus = [attendus]
    paires = []
    for i, att in enumerate(attendus):
        if not isinstance(att, dict):
            continue
        ibm = comptages_ibm[i] if i < len(comptages_ibm) else None
        if ibm is None:
            paires.append({"publication": i, "verdict": "ABSENT_DE_L_EXPORT"})
            continue
        ecarts = {k: (att.get(k), ibm.get(k)) for k in set(att) | set(ibm) if att.get(k) != ibm.get(k)}
        paires.append({
            "publication": i,
            "verdict": "IDENTIQUE" if not ecarts else "DIFFERENT",
            "n_ecarts": len(ecarts),
            "exemples_ecarts": dict(list(ecarts.items())[:5]),
        })
    identiques = sum(1 for p in paires if p["verdict"] == "IDENTIQUE")
    return {
        "job_id": archive.get("job"),
        "backend": archive.get("backend"),
        "test": archive.get("test"),
        "publications_archivees": len(attendus),
        "publications_exportees": len(comptages_ibm),
        "publications_identiques": identiques,
        "verdict": "CONCORDANCE TOTALE" if paires and identiques == len(paires)
                   else ("AUCUNE PUBLICATION" if not paires else "DIVERGENCES"),
        "detail": paires,
    }


def main() -> int:
    p = argparse.ArgumentParser(description="Compare un export IBM aux comptages archivés.")
    p.add_argument("--export", help="archive job-<id>.zip, fichier JSON ou dossier")
    p.add_argument("--archive", help="charge brute archivée (.json du dépôt)")
    p.add_argument("--exports-dir", help="dossier d'exports IBM")
    p.add_argument("--archives-dir", help="dossier des charges brutes archivées")
    p.add_argument("--json", dest="sortie", help="écrit le rapport JSON")
    a = p.parse_args()

    resultats = []
    if a.export and a.archive:
        jid, comptages = lire_export(Path(a.export))
        archive = json.loads(Path(a.archive).read_text())
        resultats.append(comparer(archive, comptages))
    elif a.exports_dir and a.archives_dir:
        arch = {p.stem: p for p in Path(a.archives_dir).glob("*.json")}
        for exp in sorted(Path(a.exports_dir).iterdir()):
            jid, comptages = lire_export(exp)
            if not jid or jid not in arch:
                resultats.append({"job_id": jid, "verdict": "ARCHIVE_INTROUVABLE",
                                  "fichier_export": str(exp)})
                continue
            resultats.append(comparer(json.loads(arch[jid].read_text()), comptages))
    else:
        print(__doc__)
        return 1

    print("=" * 74)
    print("COMPARAISON EXPORT IBM  ↔  COMPTAGES ARCHIVÉS")
    print("=" * 74)
    ok = 0
    for r in resultats:
        v = r["verdict"]
        marque = "✅" if v == "CONCORDANCE TOTALE" else "⚠️"
        if v == "CONCORDANCE TOTALE":
            ok += 1
        print(f"\n{marque} {r.get('job_id')}  [{v}]")
        if "test" in r:
            print(f"   {r.get('test')}  ·  {r.get('backend')}")
            print(f"   publications archivées : {r['publications_archivees']}"
                  f"   exportées : {r['publications_exportees']}"
                  f"   identiques : {r['publications_identiques']}")
            for d in r.get("detail", []):
                if d["verdict"] != "IDENTIQUE":
                    print(f"   ⚠️ pub #{d['publication']} : {d['verdict']}"
                          + (f" ({d.get('n_ecarts')} écarts, ex. {d.get('exemples_ecarts')})"
                             if d.get("n_ecarts") else ""))
    total = len(resultats)
    print(f"\n{'=' * 74}\nBILAN : {ok}/{total} tâche(s) en concordance totale")

    if a.sortie:
        json.dump(resultats, open(a.sortie, "w"), indent=1, ensure_ascii=False)
        print(f"→ rapport écrit : {a.sortie}")
    return 0 if ok == total and total else 1


if __name__ == "__main__":
    raise SystemExit(main())
