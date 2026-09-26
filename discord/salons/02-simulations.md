# 🗂️ SALONS À GARNIR — SIMULATIONS
## 7 salons : gcr-topologie · navier-turbulence · fusion-propulsion · nucleaire · synchrotron-24 · tissu-continuums-focal · dose12

*Chaque post contient un chiffre réellement mesuré, la commande pour le rejouer, et ce que ça ne prouve PAS.*

---

# 📌 #gcr-topologie

**GCR = Grand Collisionneur de Ratiss.** 🎯
Des masses qui se rencontrent, et ce qui en sort : pas des débris, des **trous topologiques**.

---

## 🧪 Le résultat central : l'étincelle topologique

| Paramètres | `b1_max` | Verdict |
|---|---|---|
| Témoin (A=0) | **1** | rien, le repos |
| A=10, γ=0.05 | **2** | ⚡ **étincelle : un trou apparaît** |
| A=10, γ=0.30 | **1** | γ élevé → ça s'étire, ça **ne déchire pas** |

Le γ contrôle tout : **doucement ça se déchire, fortement ça s'étire.** 💥

```bash
git clone --depth 1 https://github.com/jonathansearch/GCR && cd GCR
PYTHONPATH="$PWD:$PWD/univers" python3 -m pytest tests/ -q    # 4 passed
```

---

## 🔗 Le pont avec le labo

Le GCR alimente le **bus Omni** : l'énergie turbulente mesurée pilote un drive (cible 1e-10 à 2e-9).
C'est un des rares endroits du labo où deux dépôts se parlent vraiment. 🔌

⚠️ **Ce que ça ne prouve pas :** qu'une telle structure existe dans un univers réel. C'est un univers **virtuel**.

**Question ouverte pour toi :** à quelle valeur de γ exactement se situe la transition ? Personne ne l'a cartographié finement. 🔬

---

# 📌 #navier-turbulence

**Navier-Stokes en SPH 3D, avec une sonde quantique branchée dessus.** 🌊

---

## 💥 Le blow-up, chiffres en main

```
force ON  → vmax = 2.779   Om_max = 5654.1668   E = 34.84   C = 0.5173
force OFF → vmax = 0.0     Om = 0.0             E = 0.0     C = 1.0
```

**Reproduit bit à bit** : écart point par point `0.0000` sur les 11 points, sur une machine indépendante. ✅

```bash
git clone --depth 1 https://github.com/jonathansearch/RATISS-NAVIER && cd RATISS-NAVIER
pip install -e .
pytest tests/ -q                        # 4 passed
python3 demos/blowup.py --only ON       # la version forcée
python3 demos/blowup.py --only OFF      # le témoin
```

---

## 🧪 Le protocole du ticket V02

Question posée : *la saturation Ω est-elle physique ou numérique ?*
Test : **ν/10 + résolution ×2 + forçage boosté + contrôle de résolution.**
Critère, scellé **avant** la mesure : `Ω_max(ν/10) > 2 × Ω_max(ν)` → blow-up réel.

Résultat : `A=11259` (> 7658 ✅) · `B=19894` (×5,2 🔥) · `C=9192` (contrôle)
**Verdict : saturation numérique réfutée.**

⚠️ **Ce que ça ne prouve pas — et je le redis :** que ce soit une singularité **de Navier-Stokes**. Ce qui est établi, c'est que **réduire la viscosité ne suffit pas à expliquer la saturation**. Ce n'est pas la même phrase.

---

**Ce qu'on cherche :** quelqu'un qui refait le run **sur une autre machine** et poste sa sortie. C'est la seule chose qui manque. 🎯

---

# 📌 #fusion-propulsion

**Fusion D-T : compression → burn → rebond.** 🔥

---

## ⚛️ Chiffres du moteur ICF

```
R = 7.204 µm     T = 8.85 keV     ev = 428      Q = 86.62
14 frames · 84 flash-events
```

```bash
git clone --depth 1 https://github.com/jonathansearch/RATISS-FUSION && cd RATISS-FUSION
pip install -e .
pytest tests/ -q                # 4/4 : Bosch-Hale, froid=0, implosion, burn
python3 demos/ignition.py       # → demos/ignition_3d.html
```

---

## 🔬 Ce qu'il y a sous le capot

- sections efficaces **Bosch-Hale** (pas des formules inventées)
- critère de **Lawson**
- témoin à froid qui doit donner **zéro** — et qui donne zéro
- scène **Three.js** générée pour voir l'implosion en 3D

⚠️ **Ce que ça ne prouve pas :** qu'une ignition est atteignable en laboratoire. C'est de la **simulation**, et le labo l'écrit en toutes lettres.

**Question ouverte :** le Q plafonne à ~86 puis stabilise. Quel mécanisme limite ? Personne ne l'a isolé. 🤔

---

# 📌 #nucleaire

**Le module où la turbulence et la fusion se parlent.** ☢️

---

## 🧪 12/12 tests passent (7 fusion + 2 stellaire + 3 couplage)

```
ICF      : R = 6.273 µm    T = 10.5 keV     Q = 60.24     (14 frames, 83 flash-events)
Stellaire: R = 141.113 µm  T = 148.08 keV   Q = 2.867     (16 frames)
```

```bash
git clone --depth 1 https://github.com/jonathansearch/RATISS-NUCLEAIRE && cd RATISS-NUCLEAIRE
pip install -e .
pytest tests/ -q                # 12 passed
python3 demos/ignition.py       # ICF
python3 demos/stellar.py        # le canal stellaire
python3 demos/moteur.py         # le moteur unifié → PNG
```

---

## 🔌 Le couplage, concrètement

Le moteur unifié prend la **turbulence Navier** et l'injecte dans la **chambre de fusion** :
turbulence allumée → le burn réagit. Feedback activable/désactivable → **ablation**, pas intuition (Loi n°3 du labo).

⚠️ **Attention :** c'est un couplage **de code à code**. Il ne dit rien sur la fusion réelle.

---

**Le défi pour toi :** désactive le feedback (`feedback=False`) et regarde ce qui change. Poste la différence. 📊

---

# 📌 #synchrotron-24

**Neuf expériences. Un effondrement, un rebond, et une question de seuil.** 🕳️

---

## 📊 Les 9 expériences et leurs sorties réelles

```
s01 naissance       → 24/24 absorbés
s02 page            → réémis 24/24, bits_out_fin = 0.7344
s02b dissociation   → M_local = 0.02, I_rec = 0.7344
s03 rebond          → combat rapproché terminé
s03b résurrection   → sélection terminée
s04 lambda          → seuil de séparatrice trouvé
s05 fantôme         → 👻 un trou noir retiré continue de peser : M_fantôme = 0.12, H1 = 0.677
s06a bord           → verdict sec : ouvert vs fermé
s06b messagers      → enroulements mesurés, WIND 0/12 → 12/12 selon k
```

```bash
git clone --depth 1 https://github.com/jonathansearch/synchrotron-24 && cd synchrotron-24
for e in s01_naissance s02_page s02b_dissociation s03_rebond s03b_resurrection s04_lambda s05_fantome s06a_bord s06b_messagers; do
  python3 "experiences/$e.py"
done
```

---

## 🎯 Le résultat le plus net : la séparatrice

```
Λ = 0.000 → LIÉ (t=120)
Λ = 0.002 → LE POINT MARGINAL ⚠️
Λ = 0.005 → RIP à t=118
Λ = 0.010 → RIP à t=70.8
Λ = 0.200 → RIP à t=8.14
```

**Ma reproduction indépendante : 12 des 13 valeurs de Λ identiques au chiffre près.**
La 13ᵉ — précisément **λ = 0.002**, celle sur la frontière — diverge (`RIP` publié, `LIE` recalculé).
→ **consigné au journal des déviations.** C'est honnête, et c'est exactement le point qu'il faut retravailler. 🔬

---

## 🛰️ Le volet QPU

`qpu-bigbang/` contient des tâches réellement soumises sur `ibm_kingston` et `ibm_marrakesh`, avec identifiants et charges brutes archivés. Voir `#qpu-live`.

⚠️ **Ce que ça ne prouve pas :** que ces structures existent dans l'univers. C'est un **univers de simulation**, et le mot « observé » y désigne une sortie de code.

---

# 📌 #tissu-continuums-focal

**Le conteneur, le condensateur, les porteurs. 94 expériences.** 🔵

---

## ✅ Ce qui se reproduit **octet à octet**

`exp58`, `exp60`, `exp61`, `exp62`, `exp63` → **JSON identiques** aux versions publiées, sur une machine indépendante. ✅

```bash
git clone --depth 1 https://github.com/jonathansearch/ratiss-focal && cd ratiss-focal
cd experiences && python3 exp58_courbe_U.py      # le seuil du sanctuaire U, ~1 min
python3 exp60_forcage_flip.py && python3 exp61_rupture_U.py \
  && python3 exp62_flip_erosion.py && python3 exp63_unification_v12.py
```

---

## 📉 Et un échec, publié tel quel

```
exp61 → classe = MIXTE, réversibilité = IRRÉVERSIBLE
exp62 → classe = COUPLÉ_STRUCTUREL, critère = False
exp63 → score = 1/3
```

**Le test d'unification V12 échoue son propre critère, et il est publié.**
C'est la meilleure preuve que ce labo ne triche pas : quand ça ne marche pas, ça se dit. 💪

---

## ⚠️ Un point à corriger, signalé honnêtement

`ratiss-continuums/c01_berry2` : le script utilise un sampler **sans graine fixée** → les marges varient de 0.002 à 0.014 entre deux runs (`P00 = 0.496` publié vs `0.4938` recalculé).
Ce n'est **pas** une erreur de physique, c'est du bruit d'échantillonnage. Deux lignes suffisent à le figer (comme dans `c02`, qui, lui, est déterministe).

**Qui veut s'en occuper ?** C'est un bon premier ticket pour quelqu'un qui débarque. 🎯

---

# 📌 #dose12

**🖐️ Tu veux nous tester ? C'est ici. 12 prédictions vérifiables sur TA machine. Sans QPU. Rien à croire sur parole.**

---

## ✅ Ce qui tourne partout, sans matériel

| Dose | Contenu | Statut |
|---|---|---|
| 03 | homologie persistante (rips) | ✅ ok |
| 05 | atténuation d'erreurs | ✅ `exact = 0.1869` |
| 06 | correction d'erreurs (répétition) | ✅ ok |
| 07 | GCR v4 | ✅ ok |
| 09 | couche scalaire quantique | ✅ ok |
| 10 | diaphonie (crosstalk) | ✅ ok |
| 11 | jouets quantiques | ✅ ok |

```bash
git clone --depth 1 https://github.com/jonathansearch/ratiss-dose12 && cd ratiss-dose12
python3 dose-03-rips/rips.py
python3 dose-05-mitigation/shootout.py
python3 dose-07-gcrv4/gcrv4.py
```

---

## 🔑 Ce qui a besoin d'une clé IBM

`dose-01` (QAOA), `dose-02` (VQE), `dose-04` (canari) interrogent du **matériel réel** → ils réclament `IBM_TOKEN`.
Sans clé, ils s'arrêtent sur `KeyError: 'IBM_TOKEN'`. **C'est normal, et ce n'est pas un bug.**

---

## 🎯 Le principe de ce salon

**Ces 12 doses sont faites pour être contredites.**
Si une seule ne se reproduit pas chez toi → poste-la. Avec ta machine, ta version de Python, ta sortie complète.

**Une dose qui casse vaut une dose qui marche.** 💪
