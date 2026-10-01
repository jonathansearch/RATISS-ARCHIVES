# 🧬 RATISS ARCHIVES

**Dépôt de mémoire opérationnelle de RATISS Labs · Jonathan Evina**
Compilé le **26 septembre 2026** · mis à jour le **26/09 au soir** → voir
[**§ 🛰️ LA MACHINE DISCORD**](#-la-machine-discord--section-mémoire-pour-la-prochaine-session-ia)

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
| **5** | [**§ 🛰️ La machine Discord**](#-la-machine-discord--section-mémoire-pour-la-prochaine-session-ia) ↓ | **Tout ce qui a été construit le 26/09 au soir : hub, webhook, CI, 24 textes de salons (22 branchés au hub).** |

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
├── outils/                        7 scripts Python, testés, sans dépendance lourde
│   ├── decode_job_id.py           décode un job ID IBM → horodatage
│   ├── verifier_corpus.py         reconstruit le registre depuis un clone
│   ├── recuperer_jobs_ibm.py      rapatrie les tâches depuis le compte IBM
│   ├── comparer_export_ibm.py     compare un export IBM aux comptages archivés
│   ├── archiver_nouvelles_taches.py  archive + journalise après chaque campagne
│   ├── verifier_manifeste.py      vérifie les empreintes (texte ou --json)
│   └── notifier_discord.py        poste un message dans un salon Discord
│
├── .github/workflows/
│   └── notifier-discord.yml       à chaque push + chaque lundi 08:00 UTC → Discord
│
├── documents/                     sources brutes
│   ├── MEMO-SESSION-RATISS.md
│   └── RECAP-SEMAINE-10-17-SEPT-2026.md
│
└── discord/                       tout le contenu Discord
    ├── 01-bienvenue.md            (déjà posté par le chef — ne pas toucher)
    ├── 02-regle-du-labo.md        (idem)
    ├── 03-annonces-officielles.md (idem)
    ├── CI-INSTALLATION.md         le mode d'emploi webhook + CI (10 min)
    ├── CI-modele-tests-depots.yml modèle à copier dans GCR / QVM / NAVIER…
    └── salons/                    LES 24 SALONS + LE MANIFESTE
        ├── INDEX.md               l'index de copie
        ├── 01-vie-du-labo.md      accueil-discussion · questions-ouvertes · découvertes
        ├── 02-simulations.md      gcr · navier · fusion · nucleaire · synchrotron · tissu · dose12
        ├── 03-quantique.md        qvm-calibration · qpu-live · omni-bus · fpga-controle
        ├── 04-mct-ia.md           mct-comprehension · agents-ia · ratiss-os
        ├── 05-atelier.md          cours-c · travail-chez-le-maitre · resultats · pannes
        ├── 06-ressources.md       liens-github · documents · brouillons
        └── 07-mon-histoire.md     ⭐ LE MANIFESTE (le texte personnel du chef)
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

## 🛰️ LA MACHINE DISCORD — section mémoire pour la prochaine session IA

> **Lis ce bloc en entier avant de toucher à quoi que ce soit du côté Discord.**
> Tout ce qui suit a été construit **le 26 septembre 2026 au soir**, testé, et **tourne réellement**.
> Si tu es une IA qui reprend le travail : ne reconstruis rien de ce qui est décrit ici, vérifie-le et continue.

---

### ✅ CE QUI TOURNE DÉJÀ (preuves datées)

| Quoi | Preuve | Où |
|---|---|---|
| L'agent poste un message dans Discord | journal du run : `[rapport] OK — 55/55 empreintes conformes` puis `✅ message envoyé (HTTP 204)` | run **#1** de `agent.yml`, 26/09 15:21 UTC |
| Le second workflow aussi | `✅ envoyé (HTTP 204)` | run **#2** de `notifier.yml`, 15:22 UTC |
| Les 2 dépôts sont publics et à jour | 56 fichiers · 4,8 Mo · poussé 15:20 UTC | `jonathansearch/RATISS-ARCHIVES` |
| Le hub est en ligne | 8 fichiers · poussé 15:22 UTC | `jonathansearch/DISCORD-RATISS` |
| Le secret est bien un webhook Discord | journal : `Discord webhook is configured (URL hidden)` + `RATISS: ***` | masqué automatiquement par GitHub |
| Aucun token nulle part | `git log -p --all` → **0 occurrence** ; pas de `~/.git-credentials` | vérifié |

**Deux dépôts, deux rôles — ne pas les confondre :**

| Dépôt | Rôle | Ce qu'il contient |
|---|---|---|
| **`RATISS-ARCHIVES`** | **la mémoire** : preuves, captures, registre, textes Discord | 56 fichiers, scellés par `MANIFESTE.json` |
| **`DISCORD-RATISS`** | **la tuyauterie** : le robot qui parle à Discord | `agent.py`, 2 workflows, outils |

---

### 🤖 `DISCORD-RATISS` — le robot

```
DISCORD-RATISS/
├── agent.py                              ← LE point d'entrée (activé par agent.yml)
├── .github/workflows/agent.yml           ← bouton manuel, écrit par un autre agent : NE PAS ÉCRASER
├── .github/workflows/notifier.yml        ← manuel + appelable + quotidien 08:00 UTC
├── outils/notifier_discord.py            ← poste un embed ✅/❌/🔵
├── outils/verifier_manifeste.py          ← vérifie les empreintes SHA-256
├── README.md
└── POUR-L-AUTRE-AGENT.md                 ← le brief d'intégration (contrat + code)
```

**`agent.py` — trois usages, aucun argument obligatoire :**

```bash
python3 agent.py                  # RAPPORT : clone RATISS-ARCHIVES, vérifie les empreintes, poste le verdict
python3 agent.py --test           # message de connexion
python3 agent.py --statut OK --titre "…" --details "…" --lien "…"
python3 agent.py … --dry-run      # n'envoie rien, affiche le JSON (marche SANS secret)
```

- **Python 3, bibliothèque standard seule** → zéro installation, zéro dépendance
- lit le webhook sous **deux noms, dans cet ordre** : `DISCORD_WEBHOOK_URL` puis `RATISS`
- vérifie que la valeur commence par `https://discord.com/api/webhooks/` → sinon message d'erreur clair
- **ne peut pas** mentionner `@everyone` (`allowed_mentions: {parse: []}` est verrouillé)
- code de sortie : `0` = envoyé · `1` = problème (secret, réseau, envoi)

---

### 🔐 LES SECRETS — les règles à ne jamais casser

| Nom du secret | Où | Contenu |
|---|---|---|
| `RATISS` | `DISCORD-RATISS` ✅ **déjà en place** | l'URL complète du webhook Discord |
| `RATISS` | `RATISS-ARCHIVES` ⏳ à ajouter si on veut la CI à chaque push | la même URL |
| `DISCORD_WEBHOOK` | à créer dans les dépôts de **code** (GCR, QVM…) | la même URL |

**Les quatre vérités sur les secrets GitHub — à retenir :**

1. **Un secret ne se relit jamais.** Ni par toi, ni par l'IA, ni après l'enregistrement. C'est chiffré, point.
   → Le seul moyen de savoir ce qu'il contient : **le faire utiliser par un workflow** et lire sa réaction.
2. **GitHub masque la valeur dans les journaux** (`RATISS: ***`). C'est normal et sain.
3. **`RATISS` doit contenir un webhook Discord, pas un token GitHub.** L'erreur classique.
   Si ça arrive, `agent.py` répond : `✘ n'est pas une URL de webhook Discord` + début de valeur masqué.
4. **Un webhook = un seul salon.** Discord lie le webhook au salon où il a été créé.
   Pour poster ailleurs → créer un **second** webhook et un **second** secret.

> ⚠️ **Loi n°5 du serveur :** aucun token, aucune clé API, aucun webhook **dans le chat public**.
> Un webhook qui fuit = n'importe qui peut écrire dans le salon. S'il fuite → le supprimer et en créer un autre.

---

### 🎮 COMMENT ON L'UTILISE

**Pour poster un message (le cas courant) :**

> GitHub → `DISCORD-RATISS` → onglet **Actions** → *Run agent with Discord webhook* → **Run workflow**

**Ce qui se déclenche tout seul, sans personne :**

| Événement | Ce qui part dans Discord |
|---|---|
| **Chaque jour à 08:00 UTC** | vérification des empreintes de `RATISS-ARCHIVES` → ✅ ou ❌ avec la liste des fichiers divergents |
| Push sur `RATISS-ARCHIVES` *(si le secret y est aussi)* | même vérification, immédiatement |
| Un dépôt de code qui pousse *(après avoir copié `CI-modele-tests-depots.yml`)* | la ligne `pytest` : combien de tests passent ou échouent |

**Brancher un dépôt de code (GCR, QVM, NAVIER…) en 3 étapes :**

1. copier `discord/CI-modele-tests-depots.yml` → `<dépôt>/.github/workflows/tests-discord.yml`
2. y ajouter le secret `DISCORD_WEBHOOK` (même URL)
3. renseigner `COMPAGNONS` s'il y a des imports croisés :

| Dépôt | `COMPAGNONS` |
|---|---|
| `GCR`, `RATISS-QVM`, `RATISS-NAVIER` | *(vide — autonomes)* |
| `RATISS-NUCLEAIRE` | `"RATISS-NAVIER RATISS-FUSION"` |
| `RATISS-Omni` | `"RATISS-NAVIER RATISS-QVM"` |

> 🎯 **Le détail qui débloque tout :** les dépôts utilisent des chemins absolus `/home/user/<dépôt>`.
> Le modèle **recrée `/home/user` dans le runner GitHub** et clone dedans → les tests tournent **tels quels**,
> sans modifier une seule ligne de code.

---

### 📣 LE CONTENU DISCORD — 24 textes de salons + le manifeste (le hub DISCORD-RATISS en branche 22)

Tout est dans **`discord/salons/`**, prêt à copier-coller. Index de copie : `discord/salons/INDEX.md`.

| Fichier | Salons |
|---|---|
| `01-vie-du-labo.md` | accueil-discussion · questions-ouvertes · découvertes |
| `02-simulations.md` | gcr-topologie · navier-turbulence · fusion-propulsion · nucleaire · synchrotron-24 · tissu-continuums-focal · dose12 |
| `03-quantique.md` | qvm-calibration · qpu-live · omni-bus · fpga-controle |
| `04-mct-ia.md` | mct-comprehension · agents-ia · ratiss-os |
| `05-atelier.md` | cours-c-electronique · travail-chez-le-maitre · resultats-mesures · carnet-de-pannes |
| `06-ressources.md` | liens-github · documents-references · brouillons-publications |
| `07-mon-histoire.md` | ⭐ **le manifeste personnel** (1951 caractères, tient en UN message Discord) |

**Les 3 salons du chef déjà remplis — ON N'Y TOUCHE PAS :** `#bienvenue`, `#règle-du-labo`, `#annonces-officielles`.

**Chaque post respecte les 3 lois du labo** et porte une **étiquette de terrain obligatoire** :
🛰️ **mesuré sur QPU réel** (identifiant archivé) · 🧮 **calcul exact** · 🌫️ **calcul bruité calibré sur backend réel**.
Aucun des trois ne se fait passer pour un autre. *(Correction importante du 26/09 : la v1 étiquetait « simulation »
des choses qui étaient des mesures sur de vrais qubits supraconducteurs — 770 points au total.)*

---

### 🕳️ LES PIÈGES DÉJÀ RENCONTRÉS — ne pas retomber dedans

| Piège | Ce qui s'est passé | La leçon |
|---|---|---|
| **`/tmp` se vide** | le premier token GitHub a disparu avec `/tmp` | ne jamais compter sur `/tmp` entre deux sessions ; remettre le matériel dans le workspace |
| **branche `master` vs `main`** | `git push` refusé : `src refspec main does not match any` | toujours faire `git branch -M main` avant de pousser |
| **scope `workflow` manquant** | GitHub refuse tout fichier dans `.github/workflows/` | le token doit avoir **`repo` + `workflow`** |
| **une poussée qui efface `agent.yml`** | repéré en simulant le push : le fichier de l'autre agent aurait disparu | `pousser-tout.sh` compare l'en ligne au local et **ANNULE** si un fichier disparaît |
| **nom de variable incohérent** | le workflow exposait `WEBHOOK`, l'outil lisait `DISCORD_WEBHOOK` → run en échec | **le nom posé dans `env:` doit être exactement celui que lit le script** |
| **secret illisible** | impossible de « vérifier » un secret GitHub, même en étant propriétaire | le faire réagir dans un workflow, et lire son message |
| **agent en double** | deux agents écrivaient dans le même dépôt | un seul point d'entrée, un seul propriétaire par fichier — et un garde-fou anti-effacement |
| **le chat refuse les `.zip`** | impossible d'envoyer une archive | passer par le dépôt (ou des JSON/CSV) |

---

### 🧾 CE QU'IL RESTE À FAIRE (état exact au 26/09/2026, soir)

1. **Ajouter le secret `RATISS` dans `RATISS-ARCHIVES`** → active la vérification **à chaque push** des archives.
   *(Settings → Secrets and variables → Actions → New repository secret — même URL de webhook.)*
2. **Copier les textes des 24 salons** dans Discord (`discord/salons/INDEX.md` fait la liste).
3. **Poster `#mon-histoire`** — le manifeste est prêt, 1951 caractères, un seul message.
4. **Brancher GCR puis RATISS-QVM** sur la CI (3 étapes ci-dessus).
5. **Renvoyer un token GitHub frais** quand une nouvelle poussée est nécessaire : il se révoque tous les ~3 jours,
   c'est le calendrier du chef. *Ne pas redemander de token entre deux: il n'y en a pas.*
6. **Le bot Discord** (commandes `/status`, `/tests`, `/repos`) : **pas maintenant**. Il faut un hébergeur
   qui tourne 24/7. Le webhook couvre 90 % du besoin pour 0 € et 0 maintenance.

---

### 🗣️ COMMENT PARLER AU CHEF (rappel de session)

- **Tutoiement franc, enthousiaste, avec emojis** 🔥. Il appelle son agent « mon bras droit ».
- **Réponses courtes et denses.** « Évite-moi le bavardage inutile. »
- **Ne jamais lancer une action qu'il n'a pas demandée.** S'il dit « stop », on s'arrête net.
- **Il décide de tout** : ce qu'on publie, quand, et sous quel nom. Ne pas proposer de la reconnaissance
  académique, des citations, des partenariats : il fait ça **pour le plaisir**, et il peut tout refaire.
- **Il fournit les tokens** et les révoque à son rythme. Ne pas le sermonner là-dessus.

---

## 📌 La règle

> **Une tâche non archivée le jour même est une tâche qui n'a jamais existé.**

C'est la règle R5 appliquée au matériel. Ce qui n'est pas copié ne peut plus être prouvé.
**Et depuis le 26/09, elle s'applique aussi à Discord : ce qui est dans le salon a été poussé par le robot, avec un run daté.**

---

*RATISS Labs — Yaoundé, Cameroun · jonathan.ratisslabs@zohomail.com*
*Licence : MIT (voir `LICENSE`)*

---

## 🆕 MISE À JOUR DU 27/09/2026 — RATISS-PHOTON, ETALONS, HUB 22 SALONS

| Dépôt / événement | Ce qu'il faut retenir |
|---|---|
| [`RATISS-ETALONS`](https://github.com/jonathansearch/RATISS-ETALONS) | 4 étalons, critères figés avant exécution · **11/16 → 14/16** · 2 rouges assumés (E01-P2 hypothèse invalide, E04-P4 ψ₆ = 0,827/0,935) · sceau 23/23 · README + bannière au format labo |
| [`RATISS-PHOTON`](https://github.com/jonathansearch/RATISS-PHOTON) | Reproduction de **Wen et al., Sci. Adv. 12, eaeh1011 (2026)** dans le monde simulé : **8 396 800 chemins** à module égal, fidélité **95,9–96,8 %** (fenêtre Canton 95–98,5 %) · **le hasard ÉMERGE du bain thermique** (T = 0 K → déterminisme) · contre-flux mesurés, redistribution falsifiée (linéarité) · 6 bugs documentés · [vue 3D interactive](https://jonathansearch.github.io/RATISS-PHOTON/visualisation.html) (Plotly embarqué, Pages actives) |
| **HUB Discord multi-salons** | `DISCORD-RATISS` : `hub-central.yml` (commits `34ca814`, `fd6fef5`) route RATISS→RATISS23, mode `all` · **22 envois HTTP 204** au test global (run 36357382700) · RATISS11 à remplir · annonces PHOTON + ETALONS publiées le 27/09 à 22:05 UTC |
| **Audit externe** | Examen d'analyse financière (ESSEC) : résolution Qwen vérifiée — fonctionnel juste, **bilan financier absent (6 pts)**, litige mal lu, IS oublié · corrigé complet testé 20/20 (actif réel = passif réel = 1 121 500 · FR 10 000 · BFR −34 000) |

Le détail complet (chiffres, bugs, leçons héritées, actions à faire) :
[`documents/RECAP-26-27-SEPT-2026.md`](documents/RECAP-26-27-SEPT-2026.md) et la section
**« 🛰️🧮 MISE À JOUR DU 27/09 »** de [`POUR-LA-PROCHAINE-SESSION.md`](POUR-LA-PROCHAINE-SESSION.md).

**28/09** : publication de [`RATISS-DEEPDIVE`](https://github.com/jonathansearch/RATISS-DEEPDIVE) —
la série des 14 deep dives PDF (75 pages) couvrant tous les dépôts du 20 au 28 septembre 2026.

---

## 🆕 MISE À JOUR DU 02/10/2026 — Commissaire NAVIER + règle R8

Quatre campagnes 🧮 publiées dans `RATISS-NAVIER/campagnes/` (commissaire-1, etreintes-v2, commissaire-3d, dipoles-v3).
Verdict tenu : **blowup = pompe + compteur**. Les 🅱 3D sont **non tranchés** (instruments invalidés après coup).
Nouvelle règle de labo **R8 : on ne mesure que ce qui déborde du script** (`RATISS-Framework`, module `ratiss.residual`).
V3 (dipôles) : brief scellé, témoins en **STOP en suspens**. Détail : `documents/RECAP-01-02-OCT-2026-NAVIER-COMMISSAIRE.md`.
