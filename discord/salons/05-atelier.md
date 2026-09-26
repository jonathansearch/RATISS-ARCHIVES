# 🗂️ SALONS À GARNIR — ATELIER
## 4 salons : cours-c-electronique · travail-chez-le-maitre · resultats-mesures · carnet-de-pannes

*L'ATELIER, c'est l'ancrage matériel sous les doigts. Le labo mesure déjà sur de vrais qubits — mais via le cloud et sa file d'attente. Ici, on apprend à mesurer avec ses mains.*

---

# 📌 #cours-c-electronique

**Apprendre le C et l'électronique, pour de vrai, avec un fer à souder et un oscilloscope.** 🔧

C'est le salon du **côté matériel** du labo. Ici on ne parle pas de frameworks et d'abstractions : on parle de composants, de schémas, de tensions et de code qui doit tenir dans un microcontrôleur.

---

## 📚 Le plan, en trois couches

**1. Le langage C** — pas pour « faire du dev ». Pour **parler au matériel** :
pointeurs et adresses, registres, interruptions, gestion de la mémoire à la main.

**2. L'électronique de base** — lire un schéma, choisir une résistance, comprendre un condensateur, respecter une polarité, éviter de griller la carte. ⚡

**3. L'instrumentation** — oscilloscope, multimètre, alimentation de labo.
**Une mesure sans instrument, c'est une opinion.** Même loi que sur les qubits : déclaré vs mesuré.

---

## 🔬 Ce qui se passe ici concrètement

**Le format des posts :**
```
🧠 CE QUE J'APPRENDS :
🔌 CE QUE J'AI MONTÉ :
📉 CE QUI A GRÉSILLÉ :
❓ MA QUESTION :
```

**Les questions « bêtes » sont bienvenues.** Si tu ne comprends pas pourquoi une LED a besoin d'une résistance, pose la question — c'est une vraie question, et beaucoup de gens n'osent pas la poser. 🛡️

Le seul truc qui n'est pas toléré ici : faire semblant d'avoir compris. 🤝

---

## 🔗 Le lien direct avec le reste du labo

Le labo a déjà mesuré sur de vrais processeurs quantiques — mais **à distance**, avec un quota et une file d'attente.
Un banc à soi, c'est la même rigueur (témoins, incertitudes, répétabilité) appliquée à des objets qu'on tient dans la main.

**Et c'est le chemin pour `#fpga-controle`** : python → C → VHDL. 🛠️

---

# 📌 #travail-chez-le-maitre

**23 ans d'expérience. Formation allemande. Avenue Kennedy, Yaoundé.** 🇩🇪🇨🇲

Ce salon est le **journal d'apprentissage** d'un autodidacte chez un artisan qui sait faire.

> Pourquoi c'est important : un mois de cloud et de tracés, ça fait vivre la tête. Le fer à souder fait vivre les mains.
> Les deux ensemble, ça fait un chercheur. **Un seul des deux, ça fait quelqu'un qui se raconte des histoires.**

---

## 🛠️ Ce qu'on apprend dans un vrai atelier

- **La rigueur du geste** — un fil mal dénudé, un composant monté à l'envers, et ça ne marche pas. Le matériel ne négocie pas. 💪
- **Le diagnostic** — trouver la panne sans la voir, par déduction et par mesure. C'est exactement la compétence qui a permis de repérer `q113 / q121 / q146`, les qubits morts d'une puce IBM, **sans tirer un seul job**.
- **L'économie de moyens** — faire avec ce qu'on a, pas avec ce qu'on commanderait
- **L'humilité** — celui qui a 23 ans de métier connaît des choses qui ne sont écrites dans aucun manuel

---

## 📝 Le format du journal

```
📅 JOUR X
🔧 CE QU'ON A FAIT :
🤯 CE QUE J'AI COMPRIS (ou pas) :
⚡ LA PHRASE DU MAÎTRE :
📸 PHOTO / SCHÉMA :
```

**C'est aussi un carnet de mémoire.** Dans six mois, ces notes vaudront plus qu'un long rapport : elles montreront d'où tu viens. ❤️

---

# 📌 #resultats-mesures

**Une mesure sans incertitude n'est pas une mesure. C'est une affirmation.** 📊

Ce salon est la **traçabilité matérielle** du labo : ce qui sort d'un instrument — oscilloscope, multimètre, VNA, **ou d'un processeur quantique réel** — et pas d'un calcul.

---

## 📝 Le format obligatoire

```
📅 DATE :
🔬 INSTRUMENT :          (oscilloscope / VNA / QPU nommé : ibm_kingston, ibm_marrakesh, ibm_fez)
📐 MESURE :              valeur ± incertitude
🌡️ CONDITIONS :          ce qui peut la faire bouger
📈 TRACE :               photo, CSV, capture — ou identifiant de tâche
🔁 RÉPÉTABILITÉ :        1 fois / 3 fois / 10 fois
⚠️ CE QUI POURRAIT FAUSSER LA MESURE :
```

**La dernière ligne est la plus importante.** C'est celle qui distingue un laboratoire d'une démonstration.

---

## 🛰️ Le parc instrumental du labo, honnêtement

| Type | État | Volume |
|---|---|---|
| **QPU distants** (IBM supraconducteur, plan Open) | ✅ en service | **770 points**, 75 tâches, 3 backends |
| **Simulateurs bruités calibrés sur backends réels** | ✅ en service | radar + microscope |
| **Instruments de banc** (oscilloscope, VNA, multimètre) | 🔧 en apprentissage | — |

**Ce salon se remplira donc surtout de mesures QPU pour l'instant** — et des premières mesures de banc quand le fer à souder aura parlé. ⏳

**Ce qui est déjà écrit noir sur blanc dans les archives du labo :**
- un conducteur peut être **faux** : le VNA synthétique a servi de calibrage, il n'a pas valeur de mesure de puce
- `dt = 4 ns` a faussé une série entière de mesures → la leçon est dans `#carnet-de-pannes`

---

## 🔗 L'articulation avec les autres salons

| Salon | Type de preuve |
|---|---|
| `#découvertes` | sortie de code, avec hash |
| `#qpu-live` | tâche distante, avec identifiant et charge brute archivés |
| **`#resultats-mesures`** | **instrument — y compris un vrai QPU — avec incertitude** |

Les trois ne valent pas la même chose, et le labo ne les mélange jamais. 🔬

---

# 📌 #carnet-de-pannes

**Loi n°2 du labo : les bugs se documentent, ils ne se cachent pas.** 🐛

Ce salon est le plus utile du serveur, et celui que tout le monde veut cacher.
**Ici, on expose les pannes.**

---

## 🏆 La panne fondatrice : `dt = 4 ns`

Un décalage de pas de temps qui a faussé une série de résultats — **délais 18× trop longs**. Des heures perdues à chercher la physique, alors que le problème était dans **une ligne de configuration**.

**Ce qui a été appris :** *toujours vérifier l'unité avant de vérifier la théorie.* ⏱️
Depuis : paramètres scellés et hashés **avant** la mesure.

---

## 📋 Le format obligatoire

```
💥 SYMPTÔME :
🔍 DIAGNOSTIC :
💡 CAUSE RÉELLE :
🔧 CORRECTIF :
⏱️ TEMPS PERDU :
📌 LEÇON RETENUE :      une phrase, réutilisable
```

La ligne **« temps perdu »** n'est pas là pour faire joli : c'est un **coût**, et un coût documenté devient une décision d'ingénierie.

---

## 🎯 Le registre réel des pannes du labo (tickets ouverts et clos)

**⏱️ `dt = 4 ns` (fondateur)** — délais 18× trop longs. Clos : paramètres scellés avant mesure.

**🎲 La loterie du layout** — batch 2 tombé sur des qubits morts (`q121/q146`) : 28 publications dont une partie inexploitable. **Correctif mesuré au batch suivant** : layout forcé + REM → Bell `0.997`. Clos, méthode conservée.

**💀 Trois qubits morts sur une puce** — `q113`, `q121`, `q146` identifiés par sonde directe, **sans consommer un seul job**. Clos. La sonde reste dans la boîte à outils.

**🔁 Un détecteur réfuté par le matériel** — `β1-Hamming` mesuré sur vrais qubits : saturé (67 → 90–110) **y compris sur le témoin libre**. Cause : distributions des murs trop plates → le bruit fabrique de faux cycles. **Statut : réfuté, données conservées.** Leçon : *un détecteur se juge d'abord sur son témoin.*

**🧪 `n = 1` mentait** — batch 4 (n=1) montrait `mid > brutal` ; à n=3, `brutal > mid` **3 rondes sur 3** (3.3σ). Verdict publié : l'inversion était du bruit. Leçon : **rien sous n=3.**

**📉 La dérive de session** — `0.04` entre sessions ≫ `0.01` en intra-ronde. Ce n'est pas un bug, c'est une propriété du matériel → **autocalibration obligatoire** par session, facteur backend `kingston/marrakesh ≈ 1.4`.

**🧬 Un sampler sans graine** — `ratiss-continuums/c01_berry2` : marges variant de 0.002 à 0.014 entre deux runs. Pas une erreur de physique, mais **pas bit-reproductible**. Ticket ouvert, correctif connu (deux lignes, comme `c02`).

**🗂️ Une incohérence de documentation à trancher** — la synthèse des moissons annonce le job `dapumhj18flc739mu8lg` sur **kingston**, le fichier de données du même job déclare **marrakesh**. Un seul des deux est juste. **Ticket ouvert** — c'est exactement le genre de détail qu'on ne laisse pas passer.

**🩹 117 chemins absolus codés en dur** (`/home/user/...`) dans les dépôts → tout casse dès qu'on clone ailleurs. Ticket ouvert, bon premier chantier pour quelqu'un qui débarque. 🎯

**📐 `synchrotron` / λ = 0.002** — pile sur la séparatrice : le JSON publié dit `RIP`, le recalcul dit `LIE`. Sensible au code, pas à la physique — mais pas tranché. Ticket ouvert.

**🔍 `RATISS-Omni`** — deux révisions Git vides entrent dans le calcul du sceau du bench. Détail cosmétique ou faille ? À trancher. Ticket ouvert.

---

**Chacune de ces lignes est un ticket. Prends-en une, corrige-la, documente-la, poste.** 🛠️
