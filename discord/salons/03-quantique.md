# 🗂️ SALONS À GARNIR — QUANTIQUE
## 4 salons : qvm-calibration · qpu-live · omni-bus · fpga-controle

*Ici la frontière est vitale : **processeur quantique réel** d'un côté, **modèle calibré sur le réel** de l'autre. Chaque post dit dans quel camp il parle.*

---

# 📌 #qvm-calibration

**L'ordinateur quantique virtuel — et les jumeaux qui portent le bruit des vraies machines.** ⚛️

> ⚠️ **QVM n'est pas un QPU.** C'est un simulateur. Sa valeur : il est **calibré sur des mesures réelles**, et il les **teste hors-échantillon**. Les vraies mesures sont dans `#qpu-live`.

---

## 🔬 Le banc cQED, sorti des équations

```
f_q = 5.0 GHz   f_r = 7.0 GHz   g = 100 MHz   Q_l = 19608
χ = −5.0 MHz    T1_Purcell = 178.3 µs
T1 = 111.843 µs     T2 = 223.687 µs        (modèle Purcell + Gambetta)
5 592 portes utilisables @ 40 ns
```

**La température commande tout :**

```
10 mK  → T1 = 111.8 µs   T2 = 223.7 µs   → 5 592 portes
50 mK  → T1 = 111.8 µs   T2 = 139.3 µs   → 3 482 portes
100 mK → T1 = 111.8 µs   T2 =  11.7 µs   →   294 portes   💥
```

À 100 mK, tu perds **19×** tes portes. Ce n'est pas un détail de simulation : c'est la raison pour laquelle les vraies machines tournent à 15 mK. 🥶

**Ramsey simulée vs analytique : accord < 2 %.**

---

## 👯 Les jumeaux IBM — le nœud du salon

Un « jumeau », c'est un backend simulé qui porte **le bruit réellement moissonné** sur une puce :

```
chaîne kingston [10, 11, 18, 9, 31, 30] — données du job dapup6kak42c73cj85s0
   T1 : 125 → 371 µs        T2 : 24 → 193 µs        erreur de lecture : 0.44 → 1.78 %
courbes zz(λ) et MI(λ) mesurées sur la puce et injectées dans le modèle
```

**Le vrai test — hors-échantillon :** le jumeau est entraîné sur `λ = {0.4, 0.8, 1.2, 1.6}` et **testé sur `{0.6, 1.0, 1.4}`**.
→ ✅ **jumeau-K validé hors-échantillon** · 🟡 **limite du jumeau-M tracée, pas cachée**.

C'est la seule façon honnête de valider un simulateur : **tu l'entraînes sur une partie, tu le juges sur une autre.** 🎯

---

## 🧲 Et le fit S21 → T1/T2

Modèle de hanger (Probst 2015) : délai sur les ailes → cercle de Kasa → phase vs fréquence → diamètre → point fixe τ → polish joint.
**Validé sur trace VNA synthétique réaliste** : `Q_l 0.06 % · Q_c 1 % · τ 0.02 % · f_r 3e−8`.
→ il attend **ton** fichier CSV de banc (`f,I,Q` ou `f,mag_dB,phase_deg`) pour tourner sur des données à toi.

```bash
git clone --depth 1 https://github.com/jonathansearch/RATISS-QVM && cd RATISS-QVM
pip install -e . && pytest tests/ -q                       # 23/23
python3 demos/decoherence_microondes.py                    # T1/T2 cQED + Ramsey
python3 demos/fit_s21.py                                   # VNA → Q → T1/T2
python3 demos/purcell_protection.py                        # filtre Purcell : 111.8 → 300 µs
```

**La chaîne est cohérente de bout en bout :** le `T2 = 223.687 µs` calculé ici est la constante `T2_us = 223.7` consommée par les tests de `GCR`. Deux dépôts, une seule chaîne de mesure.

> 📌 **Pour ne pas confondre (et c'est la loi n°1 du labo) :**
> `T1 = 111.8 µs / T2 = 223.7 µs` → **modèle cQED**, pas une mesure de puce.
> `T1 = 285.4 µs`, `T2* = 70.2 µs`, écho `63.4 µs` → **mesures réelles sur vrais qubits** (voir `#tissu-continuums-focal` et `#qpu-live`).

---

# 📌 #qpu-live

**Ici, que du matériel réel. Et on écrit exactement ce que ça prouve.** 🛰️

> **Règle du salon :** une tâche est dite « exécutée sur QPU » **seulement** si l'identifiant, la date, le backend et la charge brute sont archivés. Sinon on écrit « calcul ».

---

## 📦 L'inventaire, au 26/09/2026

| | |
|---|---|
| Identifiants de tâches recensés | **86** |
| Tâches avec charge brute archivée | **75** |
| **Points de mesure sur vrais qubits supraconducteurs** | **770** |
| Campagnes | 4 |
| Backends | `ibm_kingston` · `ibm_marrakesh` · `ibm_fez` |
| Appareils | 156 qubits, **Heron r2**, États-Unis |
| Période | **26 août → 23 septembre 2026** |
| Plan | **Open** (`open-instance` sur chaque tâche) |

**Les 4 campagnes :**

```
passerelle QPU (ratiss-focal)     294 points · 64 tâches · 26→31 août
verrous QPU  (ratiss-continuums)   40 points ·  2 tâches · 22 sept
campagne big-bang (synchrotron-24) 436 points ·  7 tâches · 23 sept
radar r3 / r3b                     2 tâches soumises — résultats bloqués (quota épuisé)
```

Détail des blocs : `#synchrotron-24` et `#tissu-continuums-focal`. Ici, on parle **comptabilité et traçabilité**.

---

## 🔓 La trouvaille à partager : un job ID IBM, ça se date

Les 9 premiers caractères d'un identifiant de tâche encodent **son instant de création** :

```
créée_le = base32(id[:9]) / 8192        (secondes depuis le 01/01/1970 UTC)
```

Vérifié contre les horodatages déclarés par IBM sur **64 tâches** : écart **médian 83 ms**, maximum **782 ms**.
→ **N'importe qui peut dater un identifiant sans clé, sans compte, sans autorisation.** 🌍

```bash
python3 decode_job_id.py dapm7lj18flc739mhpl0     # → 2026-09-23 05:29:58 UTC
python3 decode_job_id.py dap7su82fm4c73f6dsrg     # → 2026-09-22 13:11:21 UTC
```

**Pourquoi ça compte :** un bout de code qui prétend avoir « tourné sur QPU » peut maintenant être **daté et confronté**. C'est de la traçabilité appliquée à l'informatique quantique. 🔍

---

## ✅ Ce qui est établi

- Les identifiants sortent du **générateur IBM** (ordre chronologique correct, 0 inversion)
- Les **calibrations par qubit** archivées sont physiquement cohérentes : **24 qubits**, `T2 ≤ 2·T1` respecté **24/24**, valeurs dans les plages Heron réelles
- **Signature matérielle** : 140 publications à deux issues examinées — **0/140 propres**, bit minoritaire médian **32 %**. Un simulateur ne produit pas ça. ✅
- Corroboration par **4 captures de la plateforme** : backends, horodatages et comptabilité du quota concordants

## ⚠️ Ce qui n'est PAS établi — et qu'on ne prétendra jamais ici

**Que les comptages publiés viennent bien de ces tâches-là.** Le lien *résultat ↔ tâche* n'est visible que par le propriétaire du compte.
→ En cours de fermeture : `comparer_export_ibm.py` compare un export officiel `job-<id>.zip` aux comptages publiés, **publication par publication**.

---

## 🧾 Contexte utile

- **Quota Open Plan :** 10 min de temps QPU par fenêtre **glissante de 28 jours** (pas un mois calendaire)
- **Deux comptes IBM** : un « passerelle » (26 août → 1er sept, les 64 tâches focal) et le compte des travaux actuels (22 → 23 sept). C'est ce qui explique la répartition des dates.
- **Prochaine cible :** `ibm_phoenix` (Nighthawk r2), annoncé sur la plateforme.
- **Routes de repli** quand le quota tombe : qBraid (chaîne validée, solde 0, devis ~5 $ lite / ~36 $ full) · AWS Braket (clés prêtes, en attente de la carte). Honnêtement : **~400 publications tirées, puis le quota mensuel est mort.**

**Loi n°1 appliquée au matériel :** `journal.usage()` est relevé à chaque rapatriement. Si le total dépasse le quota sur une fenêtre → quelque chose ne va pas, et ça se voit. 🧪

---

# 📌 #omni-bus

**Le salon où les moteurs du labo se parlent.** 🔗

> **Principe :** bus mémoire partagée + boucle fermée. Le moteur A publie une mesure, le moteur B s'en sert pour ajuster son paramètre. Ce n'est pas un pipeline figé, c'est un **système avec du retour**.

---

## 🧪 Ce qui tourne

```bash
git clone --depth 1 https://github.com/jonathansearch/RATISS-Omni && cd RATISS-Omni
pip install -e . && pytest tests/ -q           # 4/4
python3 demos/closed_loop.py                   # rampe + alerte → drive gardé
python3 redteam/bench.py                       # les 5 dépôts + sceau SHA-256
```

```
[omni] drive plein = 1.00 nN   alerte = 0.12 nN   → PNG ok
[redteam] SCEAU VERT   sceau = 79ff9ee9847330d22bed0a1101734e17
```

---

## 🔐 Le sceau, c'est le cœur du salon

Ce hash est **recalculé à chaque exécution**, à partir des tests et des empreintes de sources des 5 dépôts.
Il **se reproduit à l'identique sur une machine indépendante**. ✅
→ Touche un fichier source d'un des dépôts, **le sceau change**. C'est une alarme, pas une décoration. 🚨

---

## 🔌 Qui parle à qui, aujourd'hui

| Source | → | Cible |
|---|---|---|
| Turbulence `NAVIER` (`Om_max = 5654.1668`) | → | amplitude du drive fusion |
| Sondes `QVM` (`T1/T2` **du jumeau calibré**) | → | seuils du contrôle |
| Étincelle `GCR` (`b1 = 2–4`) | → | `Q_fus` du bus |

La consigne reste bornée dans `[1e-10, 2e-9]` ; dé-tarage ×8 quand la cohérence s'effondre.

> ⚠️ **Précision qui compte :** le `T2` qui circule dans le bus est celui du **jumeau QVM** — lui-même calibré sur des moissons réelles. Ce n'est **pas** une lecture d'instrument en direct sur un qubit. Le jour où le bus lira un QPU en direct, ça s'écrira ici.

**Le contrôle se vérifie par ablation** : avec, puis sans. 🎯

**Question ouverte :** qu'est-ce qui casse en premier si on branche un quatrième moteur ? Personne n'a essayé.

---

# 📌 #fpga-controle

**Chantier ouvert. Aucun résultat publié — et ce salon le dit d'entrée.** 🔧

> Ici on ne poste ni promesse ni roadmap marketing. On poste des schémas, du code qui compile, et des mesures.

---

## 🎯 Objectif

Descendre du **logiciel** vers le **matériel** : piloter un banc en **C** et **VHDL** vérifiable, plutôt qu'avec une couche Python.

**Pourquoi c'est utile au labo :** le labo a déjà mesuré sur de vrais qubits — mais **via le cloud**, avec une file d'attente et un quota. Un firmware qu'on flashe **chez soi** et dont on mesure la sortie à l'oscilloscope, c'est une preuve matérielle qu'on contrôle de bout en bout. C'est le prolongement naturel de « déclaré vs mesuré ». 💪

---

## 📋 Ce qui est en place / ce qui manque

| | |
|---|---|
| ✅ | un poste d'apprentissage : atelier d'électronique, avenue Kennedy, Yaoundé (23 ans de métier, formation allemande) |
| ✅ | une base en langage **C** en cours d'acquisition |
| 🚧 | premier schéma publié ici |
| 🚧 | premier bout de code qui **compile** (pas qui « devrait marcher ») |
| 🚧 | première mesure à l'oscilloscope, avec la photo |
| ❌ | aucune promesse de performance, aucune date, aucun résultat |

---

## 🤝 Ce qu'on cherche

Quelqu'un qui a **déjà** flashé un FPGA ou un microcontrôleur, et qui accepte de dire « fais plutôt comme ça, tu vas perdre trois semaines autrement ».

**Format des messages dans ce salon :**
```
🔌 SCHÉMA / CODE / MESURE   (dis lequel)
🧪 CE QUE J'AI FAIT :
📊 CE QUE ÇA DONNE :
❓ CE QUE JE NE COMPRENDS PAS :
```

**Un échec documenté vaut mieux qu'un succès raconté.** C'est la loi n°2 du labo. 🛠️
