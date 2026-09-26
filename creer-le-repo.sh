#!/usr/bin/env bash
# =============================================================================
#  creer-le-repo.sh — publie RATISS-ARCHIVES sur GitHub, en une commande.
#
#  Usage :
#    ./creer-le-repo.sh                        # avec gh (recommandé)
#    ./creer-le-repo.sh --manuel               # affiche les commandes git à faire à la main
#    ./creer-le-repo.sh --verifier             # vérifie les empreintes SHA-256
#    ./creer-le-repo.sh --nom RATISS-ARCHIVES  # nom du dépôt
#
#  Prérequis pour le mode gh : la commande `gh` installée et connectée (`gh auth login`).
#  Aucun token en dur dans ce script. Jamais.
# =============================================================================
set -euo pipefail

NOM="RATISS-ARCHIVES"
DESC="Archives opérationnelles RATISS Labs — preuves, registre des tâches IBM Quantum, identité, outils. Mémoire vérifiable, datée et rejouable."
ICI="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# --- 1. le dépôt git local existe-t-il ? ------------------------------------
init_local() {
  cd "$ICI"
  if [ ! -d .git ]; then
    git init -q
    git config user.name  "RATISS Labs"
    git config user.email "jonathan.ratisslabs@zohomail.com"
    git add -A
    git commit -q -m "RATISS Archives — compilation du 26 septembre 2026

Preuves, registre des 86 taches IBM Quantum, identite, outils, captures.
Verifiable par empreinte SHA-256 (MANIFESTE.json)." || true
    echo "  ✔ dépôt git local créé et commité"
  else
    echo "  · dépôt git local déjà présent"
  fi
}

# --- 2. vérification des empreintes -----------------------------------------
verifier() {
  cd "$ICI"
  if [ ! -f MANIFESTE.json ]; then echo "  ✘ MANIFESTE.json absent"; return 1; fi
  python3 - <<'PY'
import json, hashlib, pathlib
m = json.load(open("MANIFESTE.json"))
ok = ko = 0
for chemin, attendu in m["fichiers"].items():
    p = pathlib.Path(chemin)
    if not p.exists():
        print(f"  ✘ MANQUANT  {chemin}"); ko += 1; continue
    h = hashlib.sha256(p.read_bytes()).hexdigest()
    if h == attendu: ok += 1
    else:
        print(f"  ✘ MODIFIÉ   {chemin}"); ko += 1
print(f"\n  {ok} fichier(s) conforme(s), {ko} problème(s)")
PY
}

# --- 3. publication ----------------------------------------------------------
publier_gh() {
  command -v gh >/dev/null 2>&1 || { echo "  ✘ `gh` introuvable → utilise --manuel"; exit 1; }
  gh auth status >/dev/null 2>&1 || { echo "  ✘ `gh` non connecté → lance : gh auth login"; exit 1; }
  cd "$ICI"
  if git remote get-url origin >/dev/null 2>&1; then
    echo "  · remote origin déjà configuré → git push"
    git push -u origin "$(git branch --show-current)"
  else
    gh repo create "$NOM" --public --source=. --description "$DESC" --push
    echo "  ✔ déployé : https://github.com/$(gh api user -q .login)/$NOM"
  fi
}

manuel() {
  cat <<'EOF'

  ── Publication manuelle (3 commandes) ───────────────────────────────────
  # 1. crée un dépôt public nommé RATISS-ARCHIVES sur github.com/new
  # 2. puis, depuis ce dossier :

      git init && git add -A
      git commit -m "RATISS Archives — compilation du 26 septembre 2026"
      git branch -M main
      git remote add origin https://github.com/<TON-COMPTE>/RATISS-ARCHIVES.git
      git push -u origin main

  ── Puis, pour que ça survive hors de GitHub (recommandé) ────────────────
  • Zenodo  : connecte le dépôt GitHub à Zenodo, puis publie une "release"
              → tu obtiens un DOI permanent, citable par les moteurs et les IA.
  • SWH     : soumets l'URL du dépôt sur https://archive.softwareheritage.org/save/
              → copie universelle du code, indépendante de GitHub.

EOF
}

case "${1:-}" in
  --verifier) verifier ;;
  --manuel)   manuel ;;
  --nom)      NOM="${2:?nom manquant}"; init_local; publier_gh ;;
  ""|--go)    init_local; publier_gh ;;
  *)          echo "usage: $0 [--go|--manuel|--verifier|--nom <nom>]"; exit 1 ;;
esac
