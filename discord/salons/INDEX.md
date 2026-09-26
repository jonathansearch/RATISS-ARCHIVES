# 📣 GARNIR LES SALONS — INDEX DE COPIE (v2, corrigée)

**À faire :** ouvrir chaque fichier, copier le bloc du salon, coller dans Discord.
**À ne pas toucher :** `#bienvenue`, `#règle-du-labo`, `#annonces-officielles` (déjà en place). ✅

| Fichier | Salons couverts | Nb |
|---|---|---|
| `01-vie-du-labo.md` | accueil-discussion · questions-ouvertes · découvertes | 3 |
| `02-simulations.md` | **gcr-topologie** · navier-turbulence · fusion-propulsion · nucleaire · synchrotron-24 · tissu-continuums-focal · dose12 | 7 |
| `03-quantique.md` | qvm-calibration · qpu-live · omni-bus · fpga-controle | 4 |
| `04-mct-ia.md` | mct-comprehension · agents-ia · ratiss-os | 3 |
| `05-atelier.md` | cours-c-electronique · travail-chez-le-maitre · resultats-mesures · carnet-de-pannes | 4 |
| `06-ressources.md` | liens-github · documents-references · brouillons-publications | 3 |
| | **TOTAL** | **24** |

---

## 🔧 CORRECTION v2 — ce que la v1 avait faux

La v1 étiquetait « simulation » des choses qui sont **des mesures sur de vrais qubits supraconducteurs**.
Relecture faite dépôt par dépôt. Ce que les dépôts contiennent réellement :

| Dépôt | Ce que la v1 disait | Ce que le dépôt prouve |
|---|---|---|
| `synchrotron-24/qpu-bigbang` | « simulation » | **436 points de mesure sur 2 puces IBM** : contact zz 5σ, Page en cloche sur 2 backends, écho ×4.4, β1 réfuté sur matériel, 3 qubits morts cartographiés |
| `ratiss-focal/passerelle_quantique` | non mentionné | **294 points, 64 tâches** : PONT-60/72/76/77/T2/BERRY/BERRY-FERMÉ mesurés |
| `ratiss-continuums` | non mentionné | **40 points, 2 verrous QPU** : C01 `ibm_fez` (20 circuits), C08 `ibm_kingston` |
| `RATISS-QVM` | « virtuel » | univers virtuel **+ jumeaux calibrés sur moissons réelles**, validés **hors-échantillon** |
| `GCR` | « virtuel » ✅ | virtuel — **et son β1 est passé au test sur matériel** (réfuté, scellé, remplacé) |
| `ratiss-dose12` | « sans QPU » ✅ | exact : `$0, sans QPU`, bruit générique — et il porte le **détecteur de remplacement** |

**Chiffre consolidé : 770 points de mesure sur vrais qubits supraconducteurs · 75 tâches · 3 backends · 26 août → 23 septembre 2026.**

**Nouvelle étiquette obligatoire dans tous les posts :** 🛰️ **QPU réel** (identifiant archivé) · 🧮 **calcul exact** · 🌫️ **calcul bruité calibré sur backend réel**. Aucun des trois ne se fait passer pour un autre.

---

## ✍️ Ce qui a guidé la rédaction

1. **Loi n°1 — déclaré vs mesuré** → chaque salon porte un chiffre réellement calculé, avec la commande ou l'identifiant pour le rejouer
2. **Loi n°2 — les bugs se documentent** → `#carnet-de-pannes` ouvre sur `dt = 4 ns` et liste **11 tickets réels** (dont le détecteur réfuté et l'incohérence de backend à trancher)
3. **Loi n°3 — ce qui est prouvé devient public** → tout MIT, tout clone-able

**Et chaque post dit ce que le résultat NE prouve PAS.** C'est la ligne qui protège le labo.

---

## 📌 Les 4 salons qui portent le plus

- **`#synchrotron-24`** — la campagne QPU complète : 436 points, contact zz 5σ, Page en cloche sur deux puces
- **`#qpu-live`** — l'inventaire (770 points) + la datation des identifiants, vérifiable sans compte
- **`#gcr-topologie`** — le fil complet : trous virtuels → testés sur matériel → réfutés → remplacés → re-testés
- **`#brouillons-publications`** — les 4 textes à écrire, dont la campagne QPU (« le texte le plus fort du labo »)
