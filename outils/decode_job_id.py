#!/usr/bin/env python3
"""decode_job_id.py — RATISS Labs · R7 : un étranger peut vérifier, en une commande.

Les identifiants de tâches IBM Quantum (20 caractères, alphabet 0-9a-v) encodent
leur date de création dans leurs 9 premiers caractères.

    créé_le = base32(id[:9]) / 8192   secondes depuis le 1970-01-01 UTC

Découverte et étalonnée le 2026-09-25 sur 66 jobs IBM horodatés (écart médian
277 ms, écart max 799 ms entre l'horodatage décodé et l'horodatage serveur).

Aucune dépendance. Aucune clé. Usage :

    python3 decode_job_id.py dapm7lj18flc739mhpl0 [...]
    python3 decode_job_id.py --fichier jobs.json      # {"jobs": [...]} ou liste
    python3 decode_job_id.py --verifier <token_ibm> [--crn <Service-CRN>] [--region eu-de] <job_id>...

Le mode --verifier interroge l'API IBM Quantum : c'est la SEULE vérification qui
fait autorité sur le contenu et le statut réels d'une tâche. Sans token, on ne
peut vérifier que la *forme* et l'*horodatage* — c'est-à-dire l'existence d'une
séquence produite par le générateur IBM, pas la provenance des résultats.
"""

from __future__ import annotations

import json
import sys
from datetime import datetime, timezone

ALPHABET = "0123456789abcdefghijklmnopqrstuv"
_TICKS_PAR_SECONDE = 8192
_LONGUEUR = 20


def _base32(valeur: str) -> int:
    n = 0
    for ch in valeur:
        n = n * 32 + ALPHABET.index(ch)
    return n


def decode(job_id: str) -> datetime:
    """Renvoie la date de création encodée dans ``job_id`` (UTC)."""
    j = job_id.strip().lower()
    if not forme_valide(j):
        raise ValueError(
            f"{job_id!r} n'a pas la forme d'un job ID IBM Quantum : "
            f"{_LONGUEUR} caractères, alphabet 0-9a-v"
        )
    return datetime.fromtimestamp(_base32(j[:9]) / _TICKS_PAR_SECONDE, timezone.utc)


def forme_valide(job_id: str) -> bool:
    """Même critère que `ratiss.verify.is_ibm_job_id` (RATISS-Framework)."""
    j = (job_id or "").strip().lower()
    return len(j) == _LONGUEUR and all(c in ALPHABET for c in j)


def verifier_auprès_ibm(job_id: str, token: str, timeout: int = 30, crn: str | None = None,
                        region: str | None = None) -> dict:
    """Interroge l'API IBM Quantum — seule source qui fait autorité.

    ``crn`` (Service-CRN) identifie l'instance : nécessaire dès que le compte en
    possède plusieurs (typiquement les « open instances »). ``region`` vaut
    ``eu-de`` pour une instance hébergée en Europe.
    """
    import urllib.error
    import urllib.request

    hote = "https://quantum.cloud.ibm.com" if not region else f"https://{region}.quantum.cloud.ibm.com"
    url = f"{hote}/api/v1/jobs/{job_id}"
    entetes = {
        "Authorization": f"Bearer {token}",
        "IBM-API-Version": "2025-05-01",
        "Accept": "application/json",
    }
    if crn:
        entetes["Service-CRN"] = crn
    req = urllib.request.Request(url, headers=entetes)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return json.loads(r.read())
    except urllib.error.HTTPError as e:
        if e.code == 401:
            return {"erreur": "401 — token invalide ou révoqué (IBM ne te reconnaît pas)"}
        if e.code == 404:
            return {"erreur": "404 — cette tâche n'existe pas dans TON compte"}
        return {"erreur": f"HTTP {e.code}"}


def _charge(chemin: str) -> list[str]:
    d = json.load(open(chemin))
    if isinstance(d, dict):
        d = d.get("jobs") or d.get("job_ids") or list(d.keys())
    return [str(x) for x in d]


def main(argv: list[str]) -> int:
    if not argv:
        print(__doc__)
        return 1

    if argv[0] == "--fichier":
        for jid in _charge(argv[1]):
            try:
                print(f"{jid}  {decode(jid):%Y-%m-%d %H:%M:%S} UTC")
            except ValueError as e:
                print(f"{jid}  ✘ {e}")
        return 0

    if argv[0] == "--verifier":
        token, crn, region = argv[1], None, None
        ids: list[str] = []
        reste = argv[2:]
        i = 0
        while i < len(reste):
            if reste[i] == "--crn" and i + 1 < len(reste):
                crn = reste[i + 1]; i += 2
            elif reste[i] == "--region" and i + 1 < len(reste):
                region = reste[i + 1]; i += 2
            else:
                ids.append(reste[i]); i += 1
        for jid in ids:
            d = verifier_auprès_ibm(jid, token, crn=crn, region=region)
            if "erreur" in d:
                print(f"{jid}  ✘ {d['erreur']}")
            else:
                attendu = decode(jid)
                print(
                    f"{jid}  back={d.get('backend')}  statut={d.get('status')}  "
                    f"créé={d.get('created') or d.get('creation_date')}  "
                    f"shots={d.get('shots')}  | datation par id : {attendu:%Y-%m-%d %H:%M:%S}"
                )
        return 0

    for jid in argv:
        if jid.startswith("-"):
            print(f"option inconnue : {jid}")
            continue
        try:
            t = decode(jid)
            print(
                f"{jid}  →  {t:%Y-%m-%d %H:%M:%S} UTC  "
                f"({(datetime.now(timezone.utc) - t).days} jours)"
            )
        except ValueError as e:
            print(f"{jid}  ✘ {e}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
