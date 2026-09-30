#!/usr/bin/env python3
"""Rejoue l'étalonnage du décodeur d'ID IBM : décodé vs horodatage serveur. Zéro dépendance.
Usage : python3 outils/rejouer_etalonnage.py [preuves/qpu/horodatages-serveur-ibm.json]"""
import json, sys, statistics as st, pathlib
from datetime import datetime
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from decode_job_id import decode
f = sys.argv[1] if len(sys.argv) > 1 else "preuves/qpu/horodatages-serveur-ibm.json"
d = json.load(open(f))
e = [(datetime.fromisoformat(j["serveur_utc"]) - decode(j["job_id"])).total_seconds() * 1000
     for j in d["jobs"] if j.get("serveur_utc")]
a = [abs(x) for x in e]
print(f"{len(e)} tâches | |écart| médian {st.median(a):.1f} ms | max {max(a):.1f} ms | "
      f"signé médian {st.median(e):+.1f} ms | < 1 s : {sum(x < 1000 for x in a)}/{len(a)}")
