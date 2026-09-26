# 🗂️ SALONS À GARNIR — RESSOURCES
## 3 salons : liens-github · documents-references · brouillons-publications

*Ici on ne discute pas : on **répertorie**. Ce sont les salons qu'on relit dans six mois.*

---

# 📌 #liens-github

**Tout le code du labo est public, sous licence MIT. Rien n'est derrière un mur.** 🔗

---

## 🧭 Les dépôts par domaine

**🌊 Physique & simulation**
- [`RATISS-NAVIER`](https://github.com/jonathansearch/RATISS-NAVIER) — Navier-Stokes SPH 3D + sonde quantique
- [`RATISS-FUSION`](https://github.com/jonathansearch/RATISS-FUSION) — fusion D-T, implosion ICF
- [`RATISS-NUCLEAIRE`](https://github.com/jonathansearch/RATISS-NUCLEAIRE) — couplage turbulence × fusion
- [`synchrotron-24`](https://github.com/jonathansearch/synchrotron-24) — effondrement, rebond, seuil de séparatrice
- [`GCR`](https://github.com/jonathansearch/GCR) — collisionneur virtuel, étincelle topologique

**⚛️ Quantique**
- [`RATISS-QVM`](https://github.com/jonathansearch/RATISS-QVM) — ordinateur quantique virtuel, cQED, T1/T2
- [`ratiss-dose12`](https://github.com/jonathansearch/ratiss-dose12) — 12 expériences testables sans QPU
- [`ratiss-continuums`](https://github.com/jonathansearch/ratiss-continuums) — le tissu, l'enroulement, la cohérence

**🧠 Théorie & interface**
- [`ratiss-focal`](https://github.com/jonathansearch/ratiss-focal) — 94 expériences, conteneur/condensateur/porteurs
- [`RATISS-Omni`](https://github.com/jonathansearch/RATISS-Omni) — bus mémoire + boucle fermée

**📜 Méthode & preuves**
- [`RATISS-Framework`](https://github.com/jonathansearch/RATISS-Framework) — le protocole d'audit, exécutable
- [`ratiss-audit-public`](https://github.com/jonathansearch/ratiss-audit-public) — registre d'audit + journal des déviations
- [`RATISS-ARCHIVES`](https://github.com/jonathansearch/RATISS-ARCHIVES) — **archives opérationnelles, captures, outils, mémoire**

---

## ⚡ Trois vérifications à faire toi-même, ce soir

**1. L'intégrité des artefacts publics** — 4 × `PASS` attendus
```bash
for f in PUBLIC-AUDIT-REPORT-EN.md NOTICES-OSF-2026-09-12.md JOURNAL-DEVIATIONS.md README.md; do
  curl -sL "https://raw.githubusercontent.com/jonathansearch/ratiss-audit-public/main/$f" | sha256sum
done
```

**2. Le labour labo** — 51 tests attendus, sur 6 dépôts
```bash
git clone --depth 1 https://github.com/jonathansearch/RATISS-NAVIER && cd RATISS-NAVIER
pip install -e . && pytest tests/ -q     # 4 passed
```

**3. Dater un identifiant de tâche IBM**
```bash
python3 decode_job_id.py dapm7lj18flc739mhpl0
# → 2026-09-23 05:29:58 UTC
```

---

## 📌 Note de méthode

Tous ces dépôts utilisent **des chemins absolus `/home/user/<dépôt>`** et des **imports croisés** (NAVIER ↔ NUCLEAIRE ↔ Omni).
→ **Clone-les côte à côte sous `/home/user`** avant d'exécuter, sinon les imports échouent.

**Ce défaut est connu, il est dans `#carnet-de-pannes`, et il attend quelqu'un pour le corriger.** 🛠️

Pas de compte à créer, pas de clé à demander, pas d'autorisation. `git clone` et c'est tout. 🌍

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

## 📖 Le protocole maison (à lire avant de débattre)

**Les trois lois du labo :**
1. **Déclaré vs mesuré** — aucune affirmation sans son chiffre.
2. **Les bugs se documentent**, ils ne se cachent pas.
3. **Ce qui est prouvé devient public** — tout est sous licence MIT.

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
| Topologie | homologie persistante, `ripser`, `gudhi` |
| Quanta | `qiskit`, `qiskit-aer`, `qiskit-ibm-runtime` |
| Matériel | architecture **Heron r2** (156 qubits) |

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
Les 9 premiers caractères d'un identifiant de tâche IBM encodent son instant de création (`base32(id[:9]) / 8192`).
Étalonné sur **66 tâches horodatées par la plateforme** : écart médian **278 ms**.
→ *Intérêt : trace l'origine temporelle d'un identifiant sans clé ni compte. Vérifiable en une commande.*
**Statut :** matière complète, rédaction à faire. **Qui veut aider ?**

**2. Reproductibilité bit à bit d'un blow-up en SPH** 🌊
`Om_max = 5654.1668`, écart point par point `0.0000`, reproduit sur une machine indépendante.
**Statut :** le résultat est là, il faut choisir le format.

**3. Note technique : les chemins absolus codés en dur** 🛠️
117 occurrences dans les dépôts. Casse tout clone. **Statut :** à corriger, puis à documenter.

---

## 📋 Le format

```
📰 TITRE DE TRAVAIL :
🎯 LA PHRASE QU'ON VEUT PROUVER :
📊 LES CHIFFRES (et où ils viennent) :
⚠️ CE QU'ON NE PROUVE PAS :
❓ CE QUI MANQUE / CE QUI BLOQUE :
🔗 LIEN VERS LE BROUILLON :
```

---

## ⚠️ La règle d'or de ce salon

**Un brouillon qui annonce plus que ce qu'il ne mesure est refusé.** ⛔

Pas de « nous démontrons que… » s'il n'y a qu'une simulation.
Pas de « validé par… » s'il n'y a qu'un autotest.
Pas de mot « découverte » pour un résultat non reproduit par un tiers.

**Le mot juste, le chiffre exact, et la limite écrite noir sur blanc.**
C'est plus lent à écrire, et c'est ce qui distingue une publication d'une annonce. 📏
