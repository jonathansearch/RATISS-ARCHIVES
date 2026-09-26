#!/usr/bin/env python3
"""verifier_corpus.py — RATISS Labs · R7.

Reconstruit le registre QPU complet à partir d'un corpus cloné, et rejoue
toutes les vérifications indépendantes sur les traces de tâches IBM Quantum.

Usage :
    python3 verifier_corpus.py /chemin/vers/les/depots        # rapport
    python3 verifier_corpus.py /chemin/vers/les/depots --json registre.json

Ce que ce script VÉRIFIE (rejouable par un étranger) :
  1. forme des identifiants (20 car., alphabet 0-9a-v) ;
  2. horodatage encodé dans l'identifiant ↔ horodatage serveur enregistré ;
  3. ordre chronologique des identifiants (séquence du générateur IBM) ;
  4. cohérence nom-de-fichier ↔ identifiant interne des charges brutes ;
  5. contrainte quantique fondamentale T2 ≤ 2·T1 sur les calibrations.

Ce que ce script NE PEUT PAS vérifier (et ne prétend pas) : que les comptages
enregistrés proviennent bien de l'exécution matérielle correspondante. Cela
exige un token du compte — voir `decode_job_id.py --verifier`.
"""

from __future__ import annotations

import glob
import json
import os
import re
import sys
from collections import Counter
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from decode_job_id import ALPHABET, decode, forme_valide  # noqa: E402

ID_RE = re.compile(r"\b([a-z0-9]{20})\b")
EXEMPLES_DOC = {  # identifiants cités dans la documentation IBM, pas des runs du labo
    "d762omnq1anc738d2cj0",
}


def collecte(racine: str) -> dict[str, list[str]]:
    """Trouve les identifiants candidats et note les fichiers qui les citent."""
    trouves: dict[str, list[str]] = {}
    motifs = ("*.json", "*.md", "*.txt", "*.py", "*.tex", "*.csv")
    for motif in motifs:
        for p in glob.glob(os.path.join(racine, "**", motif), recursive=True):
            if f"{os.sep}.git{os.sep}" in p:
                continue
            try:
                txt = open(p, errors="ignore").read()
            except OSError:
                continue
            for m in set(ID_RE.findall(txt)):
                if m[0] in "cdef" and sum(c.isdigit() for c in m) >= 4 and all(c in ALPHABET for c in m):
                    trouves.setdefault(m, []).append(os.path.relpath(p, racine))
    return trouves


def main(argv: list[str]) -> int:
    if not argv:
        print(__doc__)
        return 1
    racine = argv[0]
    identifiants = collecte(racine)

    # --- 1 & 2. forme + horodatage -------------------------------------------
    lignes, rejetes = [], []
    for jid in identifiants:
        if not forme_valide(jid):
            rejetes.append(jid)
            continue
        lignes.append({"job_id": jid, "cree_utc": decode(jid).isoformat(),
                       "cite_dans": sorted(set(identifiants[jid])),
                       "exemple_doc_ibm": jid in EXEMPLES_DOC})
    lignes.sort(key=lambda r: r["cree_utc"])

    # --- 2bis. horodatage décodé ↔ horodatage serveur ------------------------
    ecarts, charges, noms_ko = [], 0, 0
    for p in glob.glob(os.path.join(racine, "**", "jobs_ibm", "*.json"), recursive=True):
        try:
            d = json.load(open(p))
        except Exception:
            continue
        if "job" not in d or "created_utc" not in d:
            continue
        charges += 1
        if d["job"] != os.path.basename(p)[: -len(".json")]:
            noms_ko += 1
        t = datetime.fromisoformat(d["created_utc"].replace(" ", "T")).timestamp()
        ecarts.append(abs(decode(d["job"]).timestamp() - t))

    # --- 3. ordre chronologique ---------------------------------------------
    seq = [r["job_id"] for r in lignes if not r["exemple_doc_ibm"]]
    inversions = sum(1 for i in range(len(seq) - 1) if seq[i] > seq[i + 1])

    # --- 5. T2 ≤ 2·T1 --------------------------------------------------------
    qubits, violations = [], 0
    for motif in ("*.json",):
        for p in glob.glob(os.path.join(racine, "**", motif), recursive=True):
            try:
                charge = json.load(open(p))
            except Exception:
                continue

            def marche(o):
                global violations
                if isinstance(o, dict):
                    if "T1" in o and "T2" in o:
                        qubits.append(o)
                        if o["T2"] > 2 * o["T1"] + 1e-9:
                            violations += 1
                    for v in o.values():
                        marche(v)
                elif isinstance(o, list):
                    for v in o:
                        marche(v)

            marche(charge)

    # --- rapport -------------------------------------------------------------
    reels = [r for r in lignes if not r["exemple_doc_ibm"]]
    print("=" * 72)
    print("REGISTRE QPU — RATISS Labs")
    print("=" * 72)
    print(f"identifiants trouvés          : {len(lignes)}")
    print(f"  dont exemples de la doc IBM : {len(lignes) - len(reels)} ({', '.join(EXEMPLES_DOC)})")
    print(f"  runs du labo                : {len(reels)}")
    if reels:
        print(f"période                      : {reels[0]['cree_utc'][:16]} → {reels[-1]['cree_utc'][:16]} UTC")
    print(f"charges brutes horodatées    : {charges}  (noms incohérents : {noms_ko})")
    print(f"écart id↔serveur             : médian {sorted(ecarts)[len(ecarts)//2]*1000:.0f} ms, "
          f"max {max(ecarts)*1000:.0f} ms" if ecarts else "écart id↔serveur             : n/a")
    print(f"ordre chronologique          : {len(seq)-1-inversions}/{len(seq)-1} paires correctes, "
          f"{inversions} inversion(s)")
    print(f"calibrations qubit           : {len(qubits)}  ·  violations T2 ≤ 2·T1 : {violations}")
    jours = Counter(r["cree_utc"][:10] for r in reels)
    print("\nactivité par jour :")
    for j, n in sorted(jours.items()):
        print(f"  {j}  {n:3d}  {'█' * n}")

    if "--json" in argv:
        sortie = argv[argv.index("--json") + 1]
        json.dump({"jobs": lignes, "jours": dict(jours),
                   "statistiques": {"total": len(lignes), "runs_labo": len(reels),
                                    "charges_brutes": charges, "violations_T2": violations}},
                  open(sortie, "w"), indent=1)
        print(f"\n→ registre écrit : {sortie}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
