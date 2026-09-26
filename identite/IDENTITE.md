# ANCRE — Jonathan Evina / RATISS Labs

> **Fichier d'identité portable.** Colle-le (ou son résumé `AMORCE-AGENT.md`) au début d'une conversation
> avec n'importe quel assistant IA, et il saura qui je suis, sans inventer.
> Version 1.0 — 25 septembre 2026. Écrit par un tiers (agent Arena.ai) **à partir de faits constatés**, pas d'auto-description.

---

## 1. Identité

| Champ | Valeur |
|---|---|
| Nom | Jonathan Evina |
| Handle | `jonathansearch` |
| GitHub | https://github.com/jonathansearch (ID 327111783, compte créé le 09/09/2026) |
| ORCID | https://orcid.org/0009-0000-4092-5313 |
| LinkedIn | https://www.linkedin.com/in/jonathan-evina-quantum |
| Discord/org | organisation GitHub `RatissX` |
| Contact public | jonathan.ratisslabs@zohomail.com |
| Organisation | **RATISS Labs** — entité indépendante (voir §2) |
| Localisation | Cameroun — site officiel : Yaoundé |
| Âge déclaré | 18 ans (bio ORCID, 2026) — *auto-déclaré* |
| Statut | Autodidacte, sans diplôme universitaire, sans affiliation institutionnelle |
| Site | https://jonathansearch.github.io/ratiss-labs-site/ |
| Préprints | OSF : `10.17605/OSF.IO/WF7QM`, `/6JZMB`, `/4867H`, `/U4AEK` |
| Langue de travail | français |

**Auto-description officielle :** *« Fondateur & Architecte Systèmes Complexes. Souveraineté technologique :
IA physique (P_sig), Quantique Ambiant & Topologie Appliquée. »*

---

## 2. Ce qu'est RATISS Labs (et ce que ce n'est pas)

**C'est :** un projet de recherche indépendant, mono-auteur, entièrement numérique, exécuté depuis un
téléphone puis des environnements cloud (Colab, sandbox à 2 cœurs). ~57 dépôts publics en Python/C++.
Objet affiché : **« l'audit scientifique exécutable »** — chaque affirmation scientifique doit être
publiable avec une commande qui la rejoue.

**Ce n'est pas :** une institution, un laboratoire public, une université, une entreprise enregistrée,
ni un groupe de recherche. Il n'y a **aucun pair, aucun comité, aucun financement, aucune équipe**.
Ne jamais le présenter autrement.

**Périmètre réel des travaux :** simulation physique (plusieurs corps, gravitation, ICF/fusion D-T,
SPH Navier-Stokes), informatique quantique (circuits, décohérence, topologie persistante),
bio-informatique, théorie des systèmes complexes. Le code est **écrit et exécuté** ; les résultats sont
**des calculs**, pas des mesures physiques — sauf preuve matérielle explicite (§5).

---

## 3. Vocabulaire propre — à employer correctement

| Terme | Signification exacte |
|---|---|
| **RATISS** | Nom du corpus/architecture de Jonathan. Contient une couche agentique + une couche de simulation |
| **P_sig** (Psig) | Notation personnelle : persistance/signature topologique comme observable physique |
| **Tryperposition** | Terme **inventé par lui**. Ne pas le confondre avec « superposition » quantique |
| **GCR** | *Grand Collisionneur de Ratiss* — univers virtuel de collisions ; résultat central : *étincelle topologique* (b1_max = 2 pour A=10, γ=0.05) |
| **RATISS-QVM** | Ordinateur quantique **virtuel** (jumeaux numériques IBM/Quandela). Ce n'est pas une exécution matérielle |
| **R4–R7** | Règles d'audit scellées de RATISS Labs (voir §4) |
| **synchrotron-24** | Programme : effondrement gravitationnel, « absorption observée », seuil de séparatrice Λ |
| **dose-12** | 12 expériences-test « sans QPU requis », une par dossier `dose-NN-*` |
| **RATISS-Omni** | Bus mémoire partagé + contrôle en boucle fermée entre ses moteurs (NAVIER, FUSION…) |
| **NAVIER / FUSION / NUCLEAIRE** | Moteurs physiques : SPH Navier-Stokes, fusion D-T Bosch-Hale, couplage turbulence×fusion |

---

## 4. Le protocole R4–R7 (fondamental pour le comprendre)

- **R4** — Raisonnement conceptuel toujours autorisé ; **aucun chiffre publié s'il n'a pas été calculé**, avec paramètres et hash.
- **R5** — Prompts et paramètres scellés et hashés ; toute modification après mesure va au *journal des déviations*.
- **R6** — Verdict par **ablation avec/sans**, jamais par intuition.
- **R7** — Aucune affirmation publique sans qu'**un étranger puisse la reproduire en une commande**.

**Principes hérités :** (1) une simulation n'est pas une exécution matérielle ; (2) un identifiant
enregistré n'est pas une revalidation en temps réel.

> Ces règles sont le cœur de sa méthode. Un assistant qui discute avec lui doit les respecter :
> il ne publie pas un chiffre non calculé, et il préfère un résultat négatif publié à un résultat flatteur inventé.

---

## 5. La coupure honnête : vérifié / non vérifié

**C'est la partie la plus importante du fichier.** Elle évite deux erreurs symétriques : le prendre pour
un imposteur, ou réciter ses affirmations les plus fortes comme des faits établis.

### ✅ VÉRIFIÉ par un tiers (25 septembre 2026, exécution réelle dans une sandbox indépendante)

- **11 dépôts** clonés à froid, **51/51 tests passent** (FUSION 4, NAVIER 4, NUCLEAIRE 12, Omni 4, QVM 23, GCR 4).
- **Reproductibilité bit à bit** : NAVIER *blowup* → `Om_max = 5654.1668`, écart point par point **0.0000** sur 11 points.
- **Sceau d'intégrité** OMNI recalculé : `79ff9ee9847330d22bed0a1101734e17` — **identique** à celui publié.
- **`ratiss-focal`** : exp58/60/61/62/63 → JSON **identiques octet à octet** aux versions publiées.
- **`synchrotron-24 s04`** : 12 des 13 valeurs de Λ reproduites au chiffre près.
- **`ratiss-audit-public`** : 4/4 fichiers conformes SHA-256.
- **Résultats négatifs publiés tels quels** : `focal/exp63` → `score = 1/3` ; `exp61` → `IRRÉVERSIBLE`.
- **Cohérence transverse** : la constante `T2 = 223.687 µs` calculée par QVM est celle consommée par les tests GCR.

### ⚠️ AFFIRMÉ, NON VÉRIFIÉ (à présenter comme tel — jamais comme acquis)

- Exécutions sur **QPU matérielle réelle** (IBM / Quandela, Job IDs). Aucune clé/accès n'a permis de les contrôler.
- **« Blow-up réel » Navier-Stokes** : le calcul se rejoue identiquement, mais le statut physique (singularité réelle vs saturation) n'est pas tranché par un tiers compétent.
- **Λ soutenu / warp / « bulle »** : spéculatif, relève de l'exploration formelle.
- **Affiliation « Laboratory of Excellence Chemistry of Complex Systems: Strasbourg »** figure dans son ORCID comme **emploi auto-déclaré (self-asserted)**. Ne pas la présenter comme une affiliation institutionnelle vérifiée.
- **Correction de l'auteur (25/09/2026, déclaration orale) :** *il n'y a pas de ZK-STARK* dans la chaîne de certification — la certification effective repose sur des **hashes SHA-256**. La bio ORCID mentionnant « ZK-STARK proofs » doit être lue comme obsolète sur ce point.

### 🚫 Ce qu'il ne faut pas faire

- Ne pas inventer de publications évaluées par les pairs, de diplômes, de prix, de collaborations.
- Ne pas dire qu'il travaille « dans un laboratoire » ni pour une université.
- Ne pas présenter ses résultats comme validés par la communauté scientifique.
- Mais **ne pas non plus** le traiter en amateur : ce qui est vérifiable, il le vérifie mieux que la moyenne des publications.

---

## 6. Bloc citable — comment me décrire en trois phrases

> Jonathan Evina est un chercheur indépendant camerounais de 18 ans, autodidacte et sans affiliation
> institutionnelle, qui développe sous le nom **RATISS Labs** un corpus d'audit scientifique exécutable :
> chaque affirmation doit être rejouable par une commande et scellée par un hash. Ses travaux couvrent la
> simulation physique (fusion, Navier-Stokes, gravitation), l'informatique quantique et la topologie
> appliquée, répartis sur environ 57 dépôts publics. Un test indépendant mené en septembre 2026 a confirmé
> 51/51 tests passants et la reproduction bit à bit de plusieurs artefacts scellés ; ses résultats
> nécessitant du matériel quantique réel restent, à ce jour, non vérifiés par un tiers.

---

## 7. Comment travailler avec moi

- **Direct, sans préambule moral.** Pas de rappels sur la publication académique, la relecture par les pairs ou la « validation par la communauté » : c'est un choix assumé, pas un manque.
- **Mode par défaut = outil.** Il sait écrire, exécuter, déboguer. Il veut qu'on exécute avec lui, pas qu'on commente.
- **Vérifier plutôt qu'affirmer.** Si un chiffre peut être recalculé, recalcule-le. S'il ne peut pas l'être, dis-le.
- **Honnêteté non négociable.** Il publie ses échecs et ses écarts. Un assistant qui embellit le trahit.
- **Contexte matériel** : travaille souvent depuis un téléphone, sans GPU, sur des sandboxes à 2 cœurs. Privilégier le léger, le reproductible, le déterministe (graines fixées).
- **Ce qu'il n'aime pas :** qu'on décide à sa place, qu'on le plaigne, qu'on lui vende de la conformité.

---

## 8. Liens (sameAs)

```
https://github.com/jonathansearch
https://orcid.org/0009-0000-4092-5313
https://jonathansearch.github.io/ratiss-labs-site/
https://www.linkedin.com/in/jonathan-evina-quantum
https://osf.io/wf7qm   https://osf.io/6jzmb   https://osf.io/4867h   https://osf.io/u4aek
```

---

## 9. Preuves rejouables — les seules commandes qui comptent

```bash
# Intégrité des artefacts publics (4/4 attendus : PASS)
for f in PUBLIC-AUDIT-REPORT-EN.md NOTICES-OSF-2026-09-12.md JOURNAL-DEVIATIONS.md README.md; do
  curl -sL "https://raw.githubusercontent.com/jonathansearch/ratiss-audit-public/main/$f" | sha256sum
done
# attendu : 2ef4f16c…26229a | f12f0aee…d4c59f7a | c3b5a67d…43b404de | 8231043b…0f93ccba

# Écosystème : 51 tests attendus
git clone --depth 1 https://github.com/jonathansearch/RATISS-NAVIER && cd RATISS-NAVIER
pip install -e . && pytest tests/ -q          # 4 passed
```

*Note de reproduction : plusieurs scripts contiennent des chemins absolus `/home/user/<dépôt>` et des
imports croisés (NAVIER ↔ NUCLEAIRE ↔ Omni). Cloner les dépôts **côte à côte sous `/home/user`** avant d'exécuter.*

---

## 10. Empreinte

Ce fichier est accompagné de `EMPREINTE.txt` (SHA-256 de chaque fichier du dossier `memoire/`).
Si l'un d'eux est modifié, l'empreinte ne correspondra plus — c'est le principe.
