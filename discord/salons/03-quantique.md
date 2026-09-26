# 🗂️ SALONS À GARNIR — QUANTIQUE
## 4 salons : qvm-calibration · qpu-live · omni-bus · fpga-controle

*Style : un chiffre, une commande, une limite honnête. Le mot « QPU » ne s'emploie que pour du matériel réel.*

---

# 📌 #qvm-calibration

**L'ordinateur quantique *virtuel* — et l'outil qui calibre le vrai.** ⚛️

> ⚠️ **QVM = simulation.** Pour le matériel réel, c'est `#qpu-live`. Ne jamais mélanger les deux.

---

## 📊 Ce que le banc sort réellement

```
cQED : f_q = 5.0 GHz   f_r = 7.0 GHz   g = 100 MHz   Q_loaded = 19608
       chi = -5.0 MHz  T1_Purcell = 178.3 µs
       T1 = 111.843 µs     T2 = 223.687 µs
```

```
T = 10 mK  → T1 = 111.8 µs  T2 = 223.7 µs   (5592 portes @ 40 ns)
T = 50 mK  → T1 = 111.8 µs  T2 = 139.3 µs   (3482 portes)
T = 100 mK → T1 = 111.8 µs  T2 =  11.7 µs   ( 294 portes)  💥
```

**Lecture :** dès 100 mK, `T2` s'effondre — tu passes de 5592 portes utilisables à moins de 300. La température n'est pas un détail, c'est **le** paramètre. 🥶

---

## 🔧 Trois tools à essayer

```bash
git clone --depth 1 https://github.com/jonathansearch/RATISS-QVM && cd RATISS-QVM
pip install -e .
pytest tests/ -q                             # 23 passed

python3 demos/effet_horizon.py               # mort et résurrection de l'intrication
python3 demos/decoherence_microondes.py      # T1/T2 cQED + Ramsey
python3 demos/fit_s21.py                     # VNA → Q → T1/T2 mesurés
python3 demos/purcell_protection.py          # filtre Purcell : T1 111.8 → 300 µs
```

En sortie de `effet_horizon` : `C: 1.0 → min = 0.000 → fin = 0.016`, et `F: 1.0 → 0.725 → 0.7267`.
**Traduction :** la cohérence meurt, puis **se récupère partiellement**. 🎭

---

## 🔗 Le détail qui compte : la constante partagée

`T2 = 223.687 µs` calculé **ici** est **exactement** la constante `T2_us = 223.7` consommée par les tests de `GCR`.
Deux dépôts, une seule chaîne de mesure. Ce n'est pas de la déco : c'est de la **cohérence transverse**. 🎯

**À faire :** refaire le fit S21 avec tes propres données VNA et comparer. Le `s21_synth.csv` est dans `demos/`.

---

# 📌 #qpu-live

**Ici, on ne parle que de matériel réel.** 🛰️

> **La règle du salon :** on écrit « tâche exécutée sur QPU » **uniquement** quand l'identifiant, la date, le backend et la charge brute sont archivés. Sinon on écrit « simulation ».

---

## 📦 L'inventaire, au 26/09/2026

| | |
|---|---|
| Identifiants de tâches archivés | **86** |
| Charges brutes horodatées (`jobs_ibm/*.json`) | **66** |
| Période couverte | **12 août → 23 septembre 2026** |
| Backends | `ibm_kingston` · `ibm_fez` · `ibm_marrakesh` |
| Appareils | 156 qubits, **Heron r2**, États-Unis |
| Plan | **Open** (mention `open-instance` sur chaque tâche) |

---

## 🔓 La trouvaille à partager : un job ID IBM, ça se date

Les 9 premiers caractères d'un identifiant de tâche IBM encodent **son instant de création** :

```
créée_le = base32(id[:9]) / 8192        (secondes depuis le 01/01/1970 UTC)
```

Vérifié sur **66 tâches horodatées par IBM** : écart **médian 278 ms**, maximum **799 ms**.
→ **N'importe qui peut dater un job ID sans clé, sans compte, sans autorisation.** 🌍

```bash
python3 decode_job_id.py dapm7lj18flc739mhpl0
# → 2026-09-23 05:29:58 UTC
```

**Pourquoi c'est important :** un bout de code qui prétend avoir « tourné sur QPU » peut maintenant être daté et confronté. C'est la traçabilité appliquée à l'informatique quantique. 🔍

---

## ✅ Ce qui est établi

- Les identifiants proviennent du **générateur IBM** (ordre chronologique : 84/84 paires correctes, 0 inversion)
- Les **calibrations par qubit** archivées sont physiquement cohérentes : **24 qubits**, `T2 ≤ 2·T1` respecté **24/24**, valeurs dans les plages Heron réelles (T1 125–371 µs, T2 24–216 µs)
- Corroboration par **4 captures de la plateforme** : backends et horodatages concordants, comptabilité du quota qui recoupe l'inventaire

## ⚠️ Ce qui n'est PAS établi — et qu'on ne prétendra jamais ici

**Que les comptages publiés proviennent bien de ces tâches.** Le lien *résultat ↔ tâche* n'est visible que par le propriétaire du compte.
→ En cours de fermeture : `comparer_export_ibm.py` compare un export officiel `job-<id>.zip` aux comptages publiés, **publication par publication**.

---

## 🧾 Contexte utile

- **Quota Open Plan :** 10 min de temps QPU par fenêtre **glissante de 28 jours** (pas un mois calendaire)
- **Deux comptes IBM distincts** : un « passerelle » (26/08 → 01/09), un pour les travaux actuels (22 → 23/09). C'est ce qui explique la répartition des dates dans les archives.
- **Prochaine cible :** `ibm_phoenix` (Nighthawk r2), annoncé sur la plateforme.

**Règle du labo appliquée au matériel :** `journal.usage()` est relevé à chaque rapatriement. Si le total dépasse le quota sur une fenêtre → quelque chose ne va pas, et ça se voit. 🧪

---

# 📌 #omni-bus

**Le salon où les moteurs du labo se parlent.** 🔗

> **Principe :** un bus mémoire partagé + une boucle fermée. Le moteur A écrit une mesure, le moteur B s'en sert pour ajuster son paramètre. Ce n'est pas un pipeline figé, c'est un **système avec du retour**.

---

## 🧪 Ce qui tourne

```
pytest tests/ -q                     # 4 passed
python3 demos/closed_loop.py         # rampe + alerte → drive gardé
python3 redteam/bench.py             # les 5 repos + sceau SHA-256
```

Sorties réelles :
```
[omni] drive plein = 1.00 nN   alerte = 0.12 nN   → PNG ok
[redteam] NAVIER ... FUSION ... NUCLEAIRE ... QVM ... Omni ...
[redteam] SCEAU VERT  sceau = 79ff9ee9847330d22bed0a1101734e17
```

---

## 🔐 Le sceau, c'est le cœur du salon

Ce hash est **recalculé à chaque exécution** du bench, à partir des tests et des empreintes de sources des 5 dépôts.

**Il se reproduit à l'identique sur une machine indépendante.** ✅
→ Si quelqu'un modifie un fichier source d'un des dépôts, **le sceau change**. C'est une alarme, pas une décoration. 🚨

```bash
python3 redteam/bench.py 2>&1 | grep SCEAU
```

---

## 🔌 Qui parle à qui, aujourd'hui

| Source | → | Cible |
|---|---|---|
| Turbulence `NAVIER` | → | amplitude du drive fusion |
| Sondes `QVM` (`T2`) | → | seuils du contrôle |
| Étincelle `GCR` | → | `Q_fus` du bus |

Le contrôle applique une **loi bornée** : la consigne reste dans `[1e-10, 2e-9]`.
Un système avec du retour, ça se vérifie par **ablation** : avec, puis sans. 🎯

**Question ouverte :** qu'est-ce qui casse en premier si on branche un quatrième moteur ? Personne n'a essayé.

---

# 📌 #fpga-controle

**Chantier ouvert. Aucun résultat publié — et ce salon le dit d'entrée.** 🔧

> Ici on ne poste ni promesse ni roadmap marketing. On poste des schémas, du code qui compile, et des mesures.

---

## 🎯 Objectif

Descendre du **logiciel** vers le **matériel** : piloter un banc avec du **C** et du **VHDL** vérifiable, plutôt qu'avec une couche Python.

**Pourquoi c'est utile au labo :** une commande Python, personne ne peut la vérifier *physiquement*. Un firmware qu'on flashe et dont on mesure la sortie à l'oscilloscope → **c'est une preuve matérielle**. C'est le prolongement naturel de la règle « déclaré vs mesuré ».

---

## 📋 Ce qui est en place / ce qui manque

| | |
|---|---|
| ✅ | un poste d'apprentissage : atelier d'électronique, avenue Kennedy, Yaoundé |
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
🔌 SCHÉMA / CODE / MESURE  (dis lequel)
🧪 CE QUE J'AI FAIT :
📊 CE QUE ÇA DONNE :
❓ CE QUE JE NE COMPRENDS PAS :
```

**Un échec documenté vaut mieux qu'un succès raconté.** C'est la loi n°2 du labo. 🛠️
