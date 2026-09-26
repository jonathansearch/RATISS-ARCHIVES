# 🧬 RATISS ARCHIVES

**Dépôt de mémoire opérationnelle de RATISS Labs · Jonathan Evina**
Compilé le **26 septembre 2026**.

> **But de ce dépôt :** ne plus jamais perdre une preuve, et ne plus jamais avoir à la rechercher.
> Tout ce qui a été produit, capturé, mesuré ou écrit entre le 12 août et le 26 septembre 2026 est ici,
> classé, nommé, daté, et **vérifié par empreinte SHA-256** (`MANIFESTE.json`).

---

## 🚀 Tu ouvres ce dépôt sans contexte ? Lis dans cet ordre

| Ordre | Fichier | Pourquoi |
|---|---|---|
| **1** | [`POUR-LA-PROCHAINE-SESSION.md`](POUR-LA-PROCHAINE-SESSION.md) | **Le résumé complet de la session du 26/09.** À coller à une IA, ou à lire soi-même. |
| **2** | [`identite/AMORCE-AGENT.md`](identite/AMORCE-AGENT.md) | Le bloc à coller en début de conversation avec n'importe quelle IA. |
| **3** | [`identite/IDENTITE.md`](identite/IDENTITE.md) | Qui je suis, ce qui est vérifié, ce qui ne l'est pas. |
| **4** | [`preuves/qpu/REGISTRE-QPU.md`](preuves/qpu/REGISTRE-QPU.md) | Les tâches IBM Quantum : décodage, corroboration, quota. |

---

## 🗂️ Organisation

```
RATISS-ARCHIVES/
├── POUR-LA-PROCHAINE-SESSION.md   ← LIRE EN PREMIER
├── MANIFESTE.json                 ← SHA-256 de chaque fichier
├── creer-le-repo.sh               ← crée/repousse le dépôt en une commande
│
├── identite/                      Qui je suis, comment le dire à une IA
│   ├── IDENTITE.md                l'ancre complète
│   ├── AMORCE-AGENT.md            la version courte à coller
│   ├── PROFIL-README.md           à mettre dans un dépôt nommé jonathansearch
│   ├── llms.txt                   fiche lisible par les robots
│   ├── person.jsonld              identité structurée schema.org
│   └── LISEZ-MOI-comment-etre-memorise.md
│
├── preuves/
│   ├── captures/                  15 photos, renommées et indexées (voir INDEX.md)
│   ├── qpu/
│   │   ├── REGISTRE-QPU.md        le rapport complet
│   │   ├── registre-jobs.json     86 identifiants datés + provenance
│   │   └── tous-les-jobs.json      idem, format liste
│   └── tests/
│       └── RAPPORT-TESTS-RATISS.md  51/51 tests, repro bit à bit
│
├── outils/                        5 scripts Python, testés, sans dépendance lourde
│   ├── decode_job_id.py           décode un job ID IBM → horodatage
│   ├── verifier_corpus.py         reconstruit le registre depuis un clone
│   ├── recuperer_jobs_ibm.py      rapatrie les tâches depuis le compte IBM
│   ├── comparer_export_ibm.py     compare un export IBM aux comptages archivés
│   └── archiver_nouvelles_taches.py  archive + journalise après chaque campagne
│
├── documents/                     sources brutes
│   ├── MEMO-SESSION-RATISS.md
│   └── RECAP-SEMAINE-10-17-SEPT-2026.md
│
└── discord/                       textes prêts à coller
    ├── 01-bienvenue.md
    ├── 02-regle-du-labo.md
    └── 03-annonces-officielles.md
```

---

## 🔐 Les résultats clés, en une page

### Découverte : les job IDs IBM encodent leur date de création

```
créé_le = base32(id[:9]) / 8192      secondes depuis le 1970-01-01 UTC
```
Étalonnée sur **66 tâches horodatées par IBM** : écart médian **278 ms**, maximum **799 ms**.
Vérifiable sans clé, sans compte, par n'importe qui, en une commande. (R7 ✅)

### Ce qui est établi

| Contrôle | Résultat |
|---|---|
| Tests des 6 dépôts physiques | **51/51** ✅ |
| `RATISS-NAVIER` blowup | reproduit **bit à bit** (`Om_max = 5654.1668`, écart 0.0000) |
| Sceau Omni redteam | `79ff9ee9847330d22bed0a1101734e17` recalculé à l'identique |
| `ratiss-focal` exp58/60/61/62/63 | JSON **identiques octet à octet** |
| `ratiss-audit-public` | **4/4** hashes conformes |
| Identifiants IBM archivés | **86** · période **12/08 → 23/09/2026** |
| Charges brutes horodatées | **66** · noms ↔ identifiants : 66/66 cohérents |
| Ordre chronologique des IDs | **84/84 paires correctes**, 0 inversion |
| Calibrations qubit (ro, T1, T2) | **24 qubits**, `T2 ≤ 2·T1` respecté 24/24 |
| Captures IBM ↔ identifiants ↔ archives | **17/17 concordances** (2 comptes) |
| Comptabilité du quota Open Plan | recoupe l'inventaire à **0,3 s/tâche près** |

### Ce qui n'est PAS établi (à ne jamais présenter comme acquis)

- Que les **comptages publiés** proviennent des tâches exactes → réglé par `comparer_export_ibm.py`.
- Le lien **résultat ↔ tâche** côté IBM (authentification requise).
- Le caractère « physique » du blow-up Navier-Stokes.
- Toute affiliation institutionnelle. **Pas de ZK-STARK** : hashes SHA-256.

---

## 🧾 Contexte IBM (à jour au 26/09/2026)

| | |
|---|---|
| Compte n°1 | `bridejackson137@gmail.com` — **travaux actuels** (22 → 23/09) — ⚠️ **suspendu**, carte à valider |
| Compte n°2 | `evinajonathan13@gmail.com` — compte « passerelle » (26/08 → 01/09) — ✅ accessible |
| Plan | **Open Plan** (gratuit), mention `open-instance` sur chaque tâche |
| Quota | 10 min de QPU par fenêtre glissante de 28 jours |
| Backends utilisés | `ibm_kingston`, `ibm_fez`, `ibm_marrakesh` — 156 qubits, Heron r2 |
| Cible suivante | `ibm_phoenix` (Nighthawk r2), annoncé sur la plateforme |

**Rappel IBM, texte exact :** *« Aucun prélèvement ne sera effectué automatiquement et vous pourrez
continuer à exécuter gratuitement vos charges de travail avec le forfait Open Plan. »*
→ La carte **débloque l'accès**, elle ne facture rien.

---

## ⚡ Reprendre le travail en 3 commandes

```bash
# 1. archiver les nouvelles tâches (après chaque campagne — compte n°2 en attendant)
export IBM_QUANTUM_TOKEN=...
python3 outils/archiver_nouvelles_taches.py --depots ~/RATISS-QVM --jours 120

# 2. vérifier le corpus
python3 outils/verifier_corpus.py ~/

# 3. comparer un export IBM aux comptages publiés (ferme R7)
python3 outils/comparer_export_ibm.py --export job-<id>.zip \
    --archive <depot>/jobs_ibm/<id>.json
```

---

## 📌 La règle

> **Une tâche non archivée le jour même est une tâche qui n'a jamais existé.**

C'est la règle R5 appliquée au matériel. Ce qui n'est pas copié ne peut plus être prouvé.

---

*RATISS Labs — Yaoundé, Cameroun · jonathan.ratisslabs@zohomail.com*
*Licence : MIT (voir `LICENSE`)*
