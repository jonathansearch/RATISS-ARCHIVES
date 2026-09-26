# 🗂️ SALONS À GARNIR — SIMULATIONS
## 7 salons : gcr-topologie · navier-turbulence · fusion-propulsion · nucleaire · synchrotron-24 · tissu-continuums-focal · dose12

*Règle de lecture de cette catégorie : pour chaque résultat, je dis **où il a été mesuré**.
Sur un vrai processeur quantique supraconducteur, ou dans un calcul. Jamais l'un pour l'autre.*

---

# 📌 #gcr-topologie

**Deux murs d'énergie percutent une nappe auto-gravitante. Le tissu vibre… ou se perce.** ⚡

Détecteur : **β1 exact** (caractéristique d'Euler sur complexe alpha) — le nombre de trous.
N = 256 particules 2D, micro-loi à cœur de Planck `F = −g/r² + k/r⁴`, `k = 0.108`.
Brutalité `B' = v·A/(w·γ)`.

---

## 📊 Résultat mesuré (batterie V3, **11 runs**, 69 s)

**L'étincelle topologique existe — en trous, pas en mots :**

```
(v=3, A=10, γ=0.05) → b1 = 4      vie 0.8 tu
(v=5, A=10, γ=0.05) → b1 = 2      vie 0.4 tu
(v=5, A=20, γ=0.05) → b1 = 3      vie 0.2 tu
seuil : B' ≳ 500
```

**Deux régimes de rupture, et c'est le résultat le plus propre :**
- `γ = 0.05` (friction faible) → **DÉCHIRURE** : trous `b1 ≥ 2`
- `γ = 0.30` (friction forte) → **ÉTIREMENT** : drop jusqu'à **0.23**, `b1 ≤ 1`, lisse — **jamais de trou**, même à A=10, v=5
→ La friction ne dissipe pas : elle **change le régime de rupture**.

**Témoin** — sans murs (A=0) : `b1_max = 0`. Sans témoin, pas de science. 🧪

**A = 3** → élastique, `b1_max = 0`, la nappe encaisse et revient : il y a un **seuil**, pas un continuum.

**Destin** : fragmentation irréversible — `r_rms 2 → 13`, système ouvert, **aucune re-cuisson** observée.

**Et une version V1 invalidée en vol** : explosion numérique (`e_kin ≈ 1e6`) → **réfutée, pas patchée**, publiquement. 🔬

```bash
git clone --depth 1 https://github.com/jonathansearch/GCR && cd GCR
pip install -e . && pytest tests/ -q          # 4/4
python3 univers/batterie_gcr.py               # 11 runs, 69 s, 0 clips
```

---

## 🛰️ Et le prolongement : le même objet, passé au test sur vraie machine

GCR est un **univers virtuel** — son propre README le dit, et c'est écrit exprès.
**Le testeur matériel est ailleurs** : c'est la campagne `synchrotron-24/qpu-bigbang`, tirée sur **vrais qubits supraconducteurs IBM**.

Là-bas, le **β1 a été mesuré sur du hardware**. Verdict : **réfuté comme détecteur**.

```
β1-Hamming sur la cellule de collision 6 qubits :
  t0 → 67 ;  doux/mid/brutal/libre/écho → 90–110
  SATURÉ PARTOUT, témoin libre compris → non discriminant
  cause mesurée : sous-graphe hypercube dense (45–59 nœuds/64), le bruit ajoute des faux cycles
  → ticket scellé : DETECTEURS_INVALIDES.md  (donnée négative conservée)
```

**Remplaçants testés et validés sur hardware** : MI / corrélateurs (batch 4) et Page-tomo (batchs 2–4).
**Remplaçant en chantier** : Rips sur distances de Hamming + **persistance** (un diagramme, pas un nombre) — voir `#dose12`.

> C'est ça, la loi n°2 : **un détecteur qui a échoué sur le matériel est publié comme les autres.** Pas caché, pas « en cours d'amélioration ». Réfuté, daté, scellé. 🎯

---

# 📌 #navier-turbulence

**Navier-Stokes en SPH 3D. Le blow-up existe-t-il, ou est-ce qu'on regarde un défaut de maille ?** 🌊

6000 particules, forçage vortex pulsé, viscosité divisée par 100. On suit l'**enstrophie Ω** (critère BKM) et l'énergie.

---

## 🧨 Le résultat

```
Om_max = 5654.1668
```

Reproduit **bit à bit** — écart point par point `0.0000`, avec le blow-up **ON** puis **OFF** (ablation). ✅
Boost de forçage : **B = 19 894 (×5.2)** avec les pulses anneau.

**Et la conclusion honnête, écrite noir sur blanc dans le dépôt :**
> La saturation est **numérique**, pas physique. On l'a prouvé par la résolution — c'est une limite de maille, pas une découverte sur les fluides.

**Contrôles systématiques** : chaque campagne a son témoin (OFF, basse résolution, sans pulses). Crashs **documentés, jamais cachés**. Garde anti-NaN en place.

```bash
git clone --depth 1 https://github.com/jonathansearch/RATISS-NAVIER && cd RATISS-NAVIER
pip install -e . && pytest tests/ -q                    # 4/4
python3 demos/blowup.py --only ON                       # Om_max = 5654.1668
```

---

## 🔗 Le fil vers le reste du labo

Dans ce dépôt vit aussi une **sonde quantique** : des traceurs de Bell à cheval sur l'écoulement (`C = 0.38`).
C'est une **simulation de corrélations quantiques** — pas une lecture d'instrument.
Les mesures sur qubits réels, elles, sont dans `#qpu-live` : **770 points** à ce jour.

**Question ouverte du salon :** la saturation à `Om_max` est-elle **seulement** numérique ? Le test à résolution doublée tranche. Personne ne l'a encore posté. 🎯

---

# 📌 #fusion-propulsion

**Fusion D-T, implosion ICF, ignition. Sans neurones — que de la physique.** ☀️

Modèle Bosch-Hale pour les sections efficaces, critère de Lawson pour l'ignition.

---

## 📊 Les chiffres mesurés (4/4 tests)

```
R  = 7.204 µm      rayon de la zone chaude
T  = 8.85 keV      température ionique
Q  = 86.62         gain fusion / énergie injectée
```

```bash
git clone --depth 1 https://github.com/jonathansearch/RATISS-FUSION && cd RATISS-FUSION
pip install -e . && pytest tests/ -q       # 4/4
```

**Statut honnête :** c'est un **modèle 0D/1D d'implosion** — pas un tokamak, pas un laser. Les nombres sont ceux du modèle, vérifiables en le relançant.
Loi de la maison : « sans neurones » → aucun réseau de neurones dans la boucle, une équation et des particules. Si le modèle se trompe, il se trompe pour une raison qu'on peut lire dans le code.

**Suite du fil :** `RATISS-NUCLEAIRE` (v0.2) branche ce moteur sur la turbulence réelle → `#nucleaire`. 🚀

---

# 📌 #nucleaire

**Le moteur unifié : la turbulence comprime, la fusion brûle, le feu repousse.** 🔥

Trois fronts ouverts dans un seul dépôt : **déplétion D/T** (le hot-spot s'auto-étouffe), **transport α diffusif**, **bremstrahlung** (≪ gain, prouvé).

---

## 📊 Mesuré (12/12 tests : 7 fusion + 2 stellaires + 3 couplage)

```
Avec forçage turbulence  → 28 événements de fusion, feedback +23 % d'énergie
Sans forçage (témoin)    → 0 événement
```

→ **Le calme n'allume pas.** C'est le témoin qui donne son sens au chiffre.

**Puis le même moteur, avec la gravité `M_enc(r)`**, effondre un nuage froid jusqu'au flash : une **supernova jouet**. 💥

```bash
git clone --depth 1 https://github.com/jonathansearch/RATISS-NUCLEAIRE && cd RATISS-NUCLEAIRE
pip install -e . && pytest tests/ -q       # 12/12
```

**Héritage scellé** : ce dépôt importe `RATISS-FUSION v0.1` en dépendance gelée — la chaîne de calcul est traçable de bout en bout, d'un dépôt à l'autre. 🔗

---

# 📌 #synchrotron-24

**Deux moitiés dans un seul dépôt : le synchrotron qui calcule, et `qpu-bigbang/` qui tire sur de vrais qubits supraconducteurs.** 🕳️🛰️

Je commence par le hardware, parce que c'est là que sont les chiffres durs.

---

## 🛰️ LA CAMPAGNE QPU — **436 points de mesure** sur vrais processeurs IBM

7 tâches sur **2 backends supraconducteurs 156 qubits** (`ibm_kingston`, `ibm_marrakesh`), 23 septembre 2026. Plan Open. Identifiants archivés dans le dépôt.

| Bloc | Points | Backend | Job |
|---|---|---|---|
| batch1 — Big Bang | 7 | marrakesh | `dapm7lj18flc739mhpl0` |
| batch2 — programme S01→S06 + WARP | 30 | kingston | `dapmb3318flc739mi1ig` |
| batch3 — revanche (layout fixe + REM) | 30 | kingston | `dapmdhcak42c73cis200` |
| batch4 — collision λ-sweep + écho | 29 | marrakesh | `dapu6sic505c73cir6f0` |
| moisson 1 (n=3) | 60 | — | `dapumhj18flc739mu8lg` |
| moisson 2 kingston (n=5) | 140 | kingston | `dapup6kak42c73cj85s0` |
| moisson 2 marrakesh (n=5) | 140 | marrakesh | `dapup6ic505c73cirsv0` |

**Le contact zz existe, et ce n'est pas du bruit** — 5σ contre des témoins, monotone en λ puis plateau :

```
marrakesh : .043 .069 .093 .125 .153 .144 .160     (60 % de la théorie)
kingston  : .091 .142 .158 .214 .204 .217 .221     (88 % de la théorie)
```

**La courbe de Page en cloche + revival — prédite AVANT le tir, puis observée :**

```
simu exacte       : pic 0.798 à λ≈0.8
mesure kingston   : pic 0.785±0.024
mesure marrakesh  : pic 0.763±0.005
```

Deux backends, même cloche. Record de stabilité : **σ = 0.005** à λ=0.8 → c'est devenu le **point de métrologie** de l'instrument.

**Résultats négatifs, scellés :**
- **β1-Hamming réfuté** comme détecteur : saturé 90–110 partout, **témoin libre compris**
- **l'inversion du batch 4 était du bruit** : n=1 mentait (mid > brutal), n=3 a tranché — `brutal > mid` **3 rondes sur 3** (3.3σ)
- **3 qubits morts cartographiés** par sonde directe : `q113`, `q121`, `q146` → chaîne de qubits forcée pour tout le reste de la campagne

**Caractérisation du matériel** (utile à tout le monde) :
- facteur backend `kingston/marrakesh ≈ 1.4` → **on ne compare pas deux backends sans calibrer**
- dérive inter-session `≈ 0.04` ≫ σ intra-ronde `≈ 0.01` → **autocalibration obligatoire**
- débit mesuré ~2000–2600 shots/s, files d'attente variables (0 à 2 h)

**Et une sonde à part :** `diag.py` inspecte la puce **sans consommer un seul job**.

---

## 🧪 Ce qui vient des simulations bruitées — et qui est étiqueté comme tel

Radar et microscope sont des **simulations bruitées calibrées sur les modèles réels** (pas des mesures) :

```
RADAR   zz(nl) : signal vivant à 8L (0.27 ≫ plancher 0.03) → horizon ≥ 8L
MICROSCOPE    : horizon extrapolé ~14L ; MI meurt AVANT zz
H exacte creuse (revival 4.44) / H bruitée monte (5.25) → Page/H seule MENT
  → LOI DU TRIO : (zz, MI, H) obligatoire
```

**Et un problème neuf ouvert au monde : la DOSIMÉTRIE DE L'INTRICATION.** Personne ne dose λ/profondeur (le QV est un chiffre abstrait). Ici on produit des courbes **dose → réponse**. Honnêteté : un supraconducteur ne stocke rien → l'appareil est un **oscilloscope**, pas une usine.

---

## 🧮 Le synchrotron lui-même (les 9 expériences de calcul)

```
s05 fantôme  → un trou noir retiré continue de peser : M_fantôme = 0.12, H1 = 0.677  👻
s04 lambda   → Λ = 0.000 LIÉ · 0.002 point marginal · 0.005 RIP à t=118 · 0.200 RIP à t=8.14
```

**Reproduction indépendante : 12 des 13 valeurs de Λ identiques au chiffre près.** La 13ᵉ — pile sur la séparatrice (λ=0.002) — diverge (`RIP` publié, `LIE` recalculé) → **journal des déviations.**

```bash
git clone --depth 1 https://github.com/jonathansearch/synchrotron-24 && cd synchrotron-24
for e in s01_naissance s02_page s02b_dissociation s03_rebond s03b_resurrection s04_lambda s05_fantome s06a_bord s06b_messagers; do python3 "experiences/$e.py"; done
```

⚠️ **La distinction qui compte :** les 436 points sont des **mesures sur vrais qubits** ; le synchrotron et le radar/microscope sont des **calculs**. Les deux vivent ici, ils ne se mélangent pas. 🔬

---

# 📌 #tissu-continuums-focal

**Le tissu, ses porteurs et ses ponts vers le vrai matériel. 94 expériences, 7 ponts mesurés sur QPU.** 🔵

---

## 🛰️ LES PONTS QPU — **334 points sur vrais qubits** (294 + 40)

Deux dépôts, une même discipline : une **prédiction écrite avant le tir**, puis une mesure sur processeur supraconducteur IBM.

**`ratiss-focal` — 294 points, 64 tâches, 26→31 août 2026 :**

```
PONT-60  T1 = 285.4 µs   R² = 0.9994        + Rabi en cosinus (simu = réel)   kingston
PONT-T2  T2* = 70.2 µs   R² = 0.96                                            marrakesh
PONT-72  T2* = 14.4 µs   →  ÉCHO : 63.4 µs  →  récupération ×4.4 par l'impulsion centrale
PONT-76  Bell + flip local : 0.98 .98 .88 .69 .41 .31   (érosion graduelle, ~1 % du simu)
PONT-77  GHZ-6 : 0.84 .41 .10 .27 .00  vs  simu 1.00 .50 .10 .30 .00
PONT-BERRY      frange en U : 1.0 → 0.49 → 1.0, réel = simu à 0.01              fez
PONT-BERRY-FERMÉ  à φ=π : lecture 0.966 (+) contre 0.028 (−), simu 1.0 / 0.0
             →  LE SENS DU PARCOURS COMPTE  (fuite ~1e-33, γ = −φ/2)           marrakesh
```

**`ratiss-continuums` — 40 points, 2 tâches, 22 septembre 2026 — ce sont les « verrous QPU » :**

```
C01  (ibm_fez, 20 circuits) : orientations (++) → 0.99 / 0.02 / 0.99 / 0.02 / 0.99
                              (+−) → plat ;  lecture Z → 0.48…0.52 partout
                              réel = simu à ~0.01   →  LA FRANGE N'EXISTE QU'EN CORRÉLATIONS
C08  (ibm_kingston) : Ramsey a = 1.2e−3 → l'ÉCHO tue a (≈0), b persiste
                              →  verrou hardware de la factorisation des échelles
```

> **Pourquoi ça compte :** la factorisation RG×QM×Thermo n'est pas validée parce qu'un modèle le dit. Elle est **verrouillée sur du matériel** : le canal gaussien est tuable, le canal exponentiel ne l'est pas. C'est la mesure qui signe. 🔐

---

## ✅ Ce qui se rejoue **octet à octet** sur une machine indépendante

`exp58`, `exp60`, `exp61`, `exp62`, `exp63` → JSON identiques aux versions publiées. ✅

## 📉 Et des échecs, publiés tels quels

```
exp61 → classe = MIXTE, réversibilité = IRRÉVERSIBLE
exp62 → classe = COUPLÉ_STRUCTUREL, critère = False
exp63 → score = 1/3        (le test d'unification échoue son propre critère)
TEST-52 (n=40) → réfute TEST-50 (n=6) : Q est MONOSTABLE, pas bistable
```

**Répliquer avant de nommer.** Le labo s'applique la règle à lui-même. 💪

## 📊 Les lois du tissu (calcul, pas QPU — c'est écrit)

```
TEST-58  sanctuaire U : sigmoïde R² = 0.964, seuil σc = 0.06
TEST-48  G sature sur un noyau absolu : 0.083  (H1 et H2 réfutées proprement)
TEST-60  flip Q piloté par la phase : P = 1.0 (14/16)
TEST-94  décohérence gravitationnelle : τ = √2/(sw·|Δf|) à ~8 % sur 18 cas
```

```bash
git clone --depth 1 https://github.com/jonathansearch/ratiss-focal && cd ratiss-focal/experiences
python3 exp58_courbe_U.py      # le seuil du sanctuaire, ~1 min
```

⚠️ **Un point à corriger, signalé honnêtement :** `continuums/c01_berry2` utilise un sampler **sans graine fixée** → marges 0.002–0.014 entre deux runs. Ce n'est pas une erreur de physique, c'est du bruit d'échantillonnage. Deux lignes suffisent (comme `c02`, déterministe). **Qui veut s'en occuper ?** 🎯

---

# 📌 #dose12

**Douze expériences testables pour 0 franc, sans QPU. Et c'est assumé : ici on calcule.** 💊

Le dépôt le dit dans sa première ligne : `$0, sans QPU` (sims exactes + bruit **générique**, pas de backend).

---

## 🧪 Le résultat qui compte le plus : la topologie qui a survécu au verdict du matériel

Rappel : sur vrais qubits, `β1-Hamming` a été **réfuté** (saturé partout, témoin compris). Le dépôt `dose-03` reprend le problème et publie **les deux versions** :

```
v1 (négative, honnête) : Rips brut sur bitstrings = AVEUGLE
      cellule λ-sweep → h0 = h1 = 1.0 partout (blob unique) ; β1 = 1.0 saturé
v2 (positive) : Rips sur la VARIÉTÉ dose→réponse (36 points : 9λ × 4nl, distance de Hellinger)

   carte              diamètre   H0 persist   H1 persist   H1 max
   exacte              0.408       1.731       0.063 (6)    0.027
   bruit faible        0.351       1.553       0.012 (3)    0.007
   bruit fort          0.230       1.193       0.007 (4)    0.005

   → effondrement : diamètre ×0.56 · H0 ×0.69 · H1 ×1/9  (les boucles s'effacent en premier)
   → bottleneck exact-vs-bruit : 0.023 → 0.043, ORDONNÉ par la dose
```

**Verdict :** le détecteur à retenir n'est pas un nombre, c'est un **triplet** — *(diamètre, H0-persist, bottleneck)*.
**Et H1 reste petit (0.063) en absolu : signal doux, pas un mur.** C'est écrit tel quel, pas maquillé. 🎯

---

## 📦 Les autres doses

```
dose-07 (GCR-V4, boîte réfléchissante) : spark v3/A10 → b1max = 2 (atténuée)
                                          spark v5/A20 → b1max = 5 (AMPLIFIÉE, la boîte concentre le violent)
                                          témoin → dérive E = 4.2 % → P09 ❌ (1e-6 exigeait Verlet, Euler fait 4 %)
                                          → prédiction fausse, modèle corrigé : LE REGISTRE FONCTIONNE
dose-10  bruit non-markovien M : écart modèle/réel marrakesh → split → 59 %
dose-06  QEC mini : logique < physique dès p ≤ 8 %
```

**Le cas `dose-07` est le plus instructif de la page :** le labo avait **pré-enregistré** un critère à 1e-6. Euler + rebonds a donné 4 %. Conclusion publiée : « P09 ❌, le modèle de départ était faux ». C'est ça, un registre de prédictions honnête : **il peut perdre**. ✅

---

> 💡 **Dans cette catégorie, trois régimes cohabitent — et le labo écrit lequel est lequel :**
> **mesuré sur vrais qubits supraconducteurs** (synchrotron-24/qpu-bigbang) ·
> **calcul exact** (synchrotron, GCR, NAVIER, FUSION) ·
> **calcul bruité calibré sur backends réels** (radar, microscope, dose12).
> Aucun des trois ne se fait passer pour un autre. 🔬
