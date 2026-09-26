# 🗂️ SALONS À GARNIR — RESSOURCES
## 3 salons : liens-github · documents-references · brouillons-publications

*Ici on ne discute pas : on **répertorie**. Ce sont les salons qu'on relit dans six mois.*

---

# 📌 #liens-github

**Tout le code du labo est public, sous licence MIT. Rien n'est derrière un mur.** 🔗

---

## 🧭 Les dépôts par domaine

**🌊 Physique & calcul**
- [`RATISS-NAVIER`](https://github.com/jonathansearch/RATISS-NAVIER) — Navier-Stokes SPH 3D, blow-up rejoué bit à bit (`Om_max = 5654.1668`)
- [`RATISS-FUSION`](https://github.com/jonathansearch/RATISS-FUSION) — fusion D-T, implosion ICF (`R = 7.204 µm`, `T = 8.85 keV`, `Q = 86.62`)
- [`RATISS-NUCLEAIRE`](https://github.com/jonathansearch/RATISS-NUCLEAIRE) — moteur unifié turbulence × fusion (28 événements, feedback +23 %)
- [`synchrotron-24`](https://github.com/jonathansearch/synchrotron-24) — 9 expériences d'effondrement **+ `qpu-bigbang/` : campagne sur vrais qubits, 436 points**
- [`GCR`](https://github.com/jonathansearch/GCR) — collisionneur **virtuel** : étincelle topologique, `β1` exact, 11 runs

**⚛️ Quantique**
- [`RATISS-QVM`](https://github.com/jonathansearch/RATISS-QVM) — ordinateur quantique virtuel, cQED, **jumeaux IBM calibrés sur moissons réelles**
- [`ratiss-focal`](https://github.com/jonathansearch/ratiss-focal) — 94 expériences, sanctuaire, **7 ponts mesurés sur vrais qubits (294 points)**
- [`ratiss-continuums`](https://github.com/jonathansearch/ratiss-continuums) — le tissu, Berry, **2 verrous QPU (40 points)**
- [`ratiss-dose12`](https://github.com/jonathansearch/ratiss-dose12) — 12 expériences testables à 0 franc, plus le détecteur topologique de remplacement

**🧠 Mémoire & interface**
- [`RATISS-Omni`](https://github.com/jonathansearch/RATISS-Omni) — bus mémoire + boucle fermée + sceau d'intégrité

**📜 Méthode & preuves**
- [`RATISS-Framework`](https://github.com/jonathansearch/RATISS-Framework) — le protocole d'audit, exécutable
- [`ratiss-audit-public`](https://github.com/jonathansearch/ratiss-audit-public) — registre d'audit + journal des déviations
- [`RATISS-ARCHIVES`](https://github.com/jonathansearch/RATISS-ARCHIVES) — **archives opérationnelles : captures, registre QPU, outils, mémoire**

---

## ⚡ Trois vérifications à faire toi-même, ce soir

**1. L'intégrité des artefacts publics** — 4 × `PASS` attendus
```bash
for f in PUBLIC-AUDIT-REPORT-EN.md NOTICES-OSF-2026-09-12.md JOURNAL-DEVIATIONS.md README.md; do
  curl -sL "https://raw.githubusercontent.com/jonathansearch/ratiss-audit-public/main/$f" | sha256sum
done
```

**2. Lancer le labo** — les tests, sur une machine à toi
```bash
git clone --depth 1 https://github.com/jonathansearch/RATISS-NAVIER && cd RATISS-NAVIER
pip install -e . && pytest tests/ -q     # 4 passed
python3 demos/blowup.py --only ON        # Om_max = 5654.1668
```

**3. Dater un identifiant de tâche IBM — sans compte**
```bash
python3 decode_job_id.py dapm7lj18flc739mhpl0     # → 2026-09-23 05:29:58 UTC
python3 decode_job_id.py dap7su82fm4c73f6dsrg     # → 2026-09-22 13:11:21 UTC
```

---

## 📌 Deux notes de méthode

**1. Chemins absolus.** Les dépôts utilisent des chemins `/home/user/<dépôt>` et des imports croisés (NAVIER ↔ NUCLEAIRE ↔ Omni).
→ **Clone-les côte à côte sous `/home/user`** avant d'exécuter, sinon les imports échouent.
Ce défaut est connu, il est dans `#carnet-de-pannes`, et il attend quelqu'un. 🛠️

**2. Ce qui consomme une clé.** Les scripts de tir QPU lisent une clé depuis la variable d'environnement `IBM_TOKEN` — **jamais commitée, jamais affichée**. Tout le reste tourne sans compte, sans clé, sans autorisation. 🌍

---

# 📌 #documents-references

**Tout ce qui est écrit, daté, et citable.** 📚

---

## 📄 Écrits du labo

| Titre | Référence |
|---|---|
| Tryperposition Framework — *Thermodynamic Emergence of Time in Hybrid Quantum Systems* | [10.17605/OSF.IO/U4AEK](https://doi.org/10.17605/OSF.IO/U4AEK) |
| Révolution quantique pour le drug design — 20 mutants p53 | [10.17605/OSF.IO/4867H](https://doi.org/10.17605/OSF.IO/4867H) |
| Préprint | [10.17605/OSF.IO/WF7QM](https://doi.org/10.17605/OSF.IO/WF7QM) |
| Préprint | [10.17605/OSF.IO/6JZMB](https://doi.org/10.17605/OSF.IO/6JZMB) |

**Identifiants :**
- ORCID : [`0009-0000-4092-5313`](https://orcid.org/0009-0000-4092-5313)
- Site du labo : [jonathansearch.github.io/ratiss-labs-site](https://jonathansearch.github.io/ratiss-labs-site/)

---

## 🗂️ Les documents internes qui font référence

| Document | Ce qu'il contient | Où |
|---|---|---|
| `RAPPORT_DECOUVERTES.md` | les 7 découvertes de la campagne QPU (D1→D7), avec preuves et limites | `synchrotron-24/qpu-bigbang/` |
| `SYNTHESE_MOISSONS.md` | exploitation des moissons : zz(λ), Page(λ), horizons, dérive | idem |
| `PASSERELLE-REEL.md` | les 7 ponts QPU mesurés + tous les outils en ligne gratuits pour confronter au réel | `ratiss-focal/` |
| `DETECTEURS_INVALIDES.md` | le détecteur réfuté, sa cause mesurée et ses remplaçants | `synchrotron-24/qpu-bigbang/qpu-collision/` |
| `REGISTRE-QPU.md` | registre des tâches, comptabilité du quota, limites | `RATISS-ARCHIVES/preuves/qpu/` |
| `JOURNAL-DEVIATIONS.md` | tout ce qui n'a pas reproduit, publié | `ratiss-audit-public` |

---

## 📖 Le protocole maison (à lire avant de débattre)

**Les trois lois du labo :**
1. **Déclaré vs mesuré** — aucune affirmation sans son chiffre.
2. **Les bugs se documentent**, ils ne se cachent pas.
3. **Ce qui est prouvé devient public** — tout est sous licence MIT.

**Les étiquettes obligatoires — un résultat se range dans UNE catégorie :**
- 🛰️ **mesuré sur QPU réel** (identifiant archivé)
- 🧮 **calcul exact** (rejouable bit à bit)
- 🌫️ **calcul bruité calibré sur un backend réel** (modèle, pas mesure)

**Deux principes hérités :**
- Une **simulation** n'est pas une exécution matérielle.
- Un **identifiant de tâche** n'est pas une revalidation en temps réel.

---

## 🧪 Références techniques réellement utilisées

| Domaine | Référence |
|---|---|
| Sections efficaces fusion | **Bosch-Hale** |
| Critère d'ignition | **Lawson** |
| Décohérence cQED | **Purcell** · **Gambetta** |
| Résonateur / extraction Q | **Probst 2015** (cercle de Kasa) |
| Topologie | homologie persistante, complexe alpha, `ripser`, `gudhi` |
| Quanta | `qiskit`, `qiskit-aer`, `qiskit-ibm-runtime` |
| Matériel | architecture **Heron r2** (156 qubits), 15 mK |

---

## 📥 Le format des contributions

```
📄 TITRE :
🔗 LIEN :
🧪 TYPE :        papier / doc / tutoriel / article
🎯 POURQUOI ÇA SERT ICI :
⏱️ TEMPS DE LECTURE :
⭐ NOTE :         à quel point c'est utile (1-5)
```

**Règle du salon :** un lien sans phrase expliquant **pourquoi** il est utile sera supprimé. On n'entasse pas, on trie.

---

# 📌 #brouillons-publications

**Ce qui est en cours d'écriture. Visible, modifiable, critiquable — avant publication.** ✍️

> **Pourquoi ce salon existe :** un texte publié sans relecture extérieure contient toujours une erreur qu'un lecteur aurait vue en dix minutes.
> Ici, on expose le brouillon **avant** de figer quoi que ce soit.

---

## 📝 En chantier

**1. Datation et audit de tâches IBM Quantum à partir de l'identifiant seul** ⭐
Les 9 premiers caractères d'un identifiant encodent son instant de création : `base32(id[:9]) / 8192`.
Étalonné sur **64 tâches horodatées par IBM** : écart médian **83 ms**, maximum **782 ms**.
→ *Un identifiant devient datable et confrontable sans clé ni compte. Vérifiable en une ligne.*
**Statut :** matière complète, rédaction à faire. **Qui veut aider ?**

**2. Campagne de mesures sur processeurs supraconducteurs 156 qubits** 🛰️
770 points de mesure, 4 campagnes, 3 backends, identifiants archivés.
Résultats phares : contact zz **5σ** (88 % de la théorie sur un backend) · courbe de Page en cloche **reproduite sur 2 puces** (pic 0.785 / 0.763) · récupération par écho **×4.4** · Berry fermé : **le sens compte** (0.966 vs 0.028).
Inclut **les échecs** : détecteur réfuté, qubits morts, inversion tranchée par la statistique.
**Statut :** les chiffres sont là, il manque la rédaction. **C'est le texte le plus fort du labo.**

**3. Dosimétrie de l'intrication — un problème neuf** 🎚️
Personne ne dose λ/profondeur (le quantum volume est un chiffre abstrait). Ici : des courbes **dose → réponse**, avec un instrument dont l'instrumentation est documentée (témoins, autocalibration, dérive).
**Statut :** méthode et données en place, angle à choisir.

**4. Les chemins absolus codés en dur : 117 occurrences, un cas d'école** 🛠️
Pourquoi un dépôt scientifique doit être clonable partout. Petit texte, forte utilité. **Statut :** à corriger d'abord, à documenter ensuite.

---

## 📋 Le format

```
📰 TITRE DE TRAVAIL :
🏷️ TERRAIN :            QPU réel / calcul exact / calcul bruité
🎯 LA PHRASE QU'ON VEUT PROUVER :
📊 LES CHIFFRES (et où ils viennent) :
⚠️ CE QU'ON NE PROUVE PAS :
❓ CE QUI MANQUE / CE QUI BLOQUE :
🔗 LIEN VERS LE BROUILLON :
```

---

## ⚠️ La règle d'or de ce salon

**Un brouillon qui annonce plus que ce qu'il ne mesure est refusé.** ⛔

Pas de « nous démontrons que… » s'il n'y a qu'un calcul.
Pas de « mesuré sur QPU » sans identifiant de tâche archivé.
Pas de « validé par… » s'il n'y a qu'un autotest.
Pas de mot « découverte » pour un résultat non reproduit par un tiers.

**Le mot juste, le chiffre exact, et la limite écrite noir sur blanc.**
C'est plus lent à écrire, et c'est ce qui distingue une publication d'une annonce. 📏
