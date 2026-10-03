# 🤖 RÉCAP 02–03/10/2026 — RATISS LABS AGENT

Dépôt : https://github.com/jonathansearch/RATISS-LABS-AGENT
État relevé le 03/10/2026 (lecture seule, rien modifié dans le dépôt agent pendant ce relevé).

## 1. Ce qui a été fait

| Quand | Quoi | Qui | Commit / PR |
|---|---|---|---|
| 02/10 | Création du dépôt + catalogue v0 (69 dépôts) | Agent Arena | `51a88c3` |
| 02/10 | Campagne complète : 84 dépôts vérifiés, README et licences lus, `MONTAGE.md` (12 étapes) | Agent Arena | `61e981b` |
| 02/10 | 2e passe : `VERSIONS.md` (Python 3.12, Node ≥ 22.19), toutes les jonctions documentées | Agent Arena | `d56632f` |
| 02/10 | Docs : `allowed-tools` + Event = CloudEvents avec `traceparent` | Agent Arena | `71d2722` |
| 02/10 | **Phase 0, les 6 contrats** : Skill = Agent Skills, Tool = MCP, Event = CloudEvents ; extensions dans `x-ratiss` | OpenHands, **fusionné par le chef** | PR #2 → `9d8f990` |
| 02/10 | **Phase 1, noyau mock** : LangGraph + registre + run tracé, appel modèle verrouillé, 107 tests | OpenHands, vérifié et fusionné par Arena | PR #3 → `bce0e64` |
| 02/10 | `ETAT-DU-PROJET.md` + `PROMPT-GLM-RESTE-A-FAIRE.md` (étapes A à L) | Agent Arena | `65ba507`, `12f9e87` |
| 03/10 | **Étape A, socle Docker** (postgres + pgvector, redis, RustFS, preflight) | GLM | **PR #4 ouverte** |
| 03/10 | **Étape B, Model Gateway** (LiteLLM 1.103.2, 3 alias, budget) | GLM | **PR #5 ouverte** (empilée sur la #4) |
| 03/10 | **Étape C, MCP Gateway** (ContextForge 1.0.11, filesystem, git, fetch, arxiv, github en option) | GLM | **PR #6 ouverte** (empilée sur la #5) |

`main` = **`12f9e87`**. PR #1 fermée (remplacée par la #2).

## 2. Les PR de GLM : ce qu'elles déclarent (relevé, non re-testé)

| PR | pytest déclaré | Limites avouées par GLM |
|---|---|---|
| #4 (A) | 107 passed | Docker absent de son espace de travail → `compose up` non lancé ; preflight en ÉCHEC chez lui (3 Go de RAM), PASS attendu chez le chef |
| #5 (B) | 123 passed | Proxy non démarré ; le refus d'un budget à 0 côté proxy reste à confirmer au premier lancement ; modèle `glm-4.6` = proposition |
| #6 (C) | 152 passed | Jeton du serveur virtuel = JWT admin provisoire (le jeton runtime viendra à l'étape E) ; versions des serveurs de base épinglées hors `VERSIONS.md` |

**Rien n'a encore tourné dans Docker pour de vrai.** Les contrôles de passage des étapes A à C restent à faire sur la machine du chef.

### Les décisions que GLM attend du chef
1. **Ordre de fusion obligatoire : #4, puis #5, puis #6** (les branches sont empilées).
2. Redis `7.4-alpine` : à valider.
3. Budget `RATISS_BUDGET_USD=10` par défaut : à confirmer.
4. Modèle principal `glm-4.6` : à valider.
5. Serveur GitHub MCP : l'activer (`COMPOSE_PROFILES=github` + jeton à permissions minimales) ou le laisser désactivé en V1 ?
6. Versions des serveurs de base (filesystem 2026.8.31, git et fetch 2026.8.18, arxiv 0.7.3) : à valider.
7. Images hétérogènes (Debian slim pour les ponts, UBI officielle pour la passerelle) : à accepter ?

## 3. Ce qui reste (voir `PROMPT-GLM-RESTE-A-FAIRE.md` dans le dépôt)

- D : admission des outils ;
- E : deepagents + checkpoint PostgreSQL ;
- **F : politique OPA + approbation** (pièce maison n° 1) ;
- G : sandboxes ;
- **H : provenance SHA-256 chaînée** (pièce maison n° 2) ;
- I : skills ;
- J : API + interface ;
- K : profils métier ;
- **L : installation sur le PC du chef** (prévue pour DeepSeek).

**Plan du chef :** GLM construit, puis DeepSeek corrige les derniers bugs et installe. Le chef a aussi, sur papier, des idées nouvelles pour l'agent, à intégrer **une fois que la base marche**.

## 4. Règles de travail établies pendant ces 2 jours

- L'agent de construction **ne fusionne jamais**. C'est le chef qui fusionne, ou l'agent Arena par délégation explicite du chef.
- Les contrats (`contrats/`) et les docs Arena (`CATALOGUE`, `MONTAGE`, `COMPATIBILITE`, `VERSIONS`, `LICENCES`, `SOURCES`) ne sont modifiés que par décision.
- Aucune clé dans git ; seul `.env.example` est versionné.
- Chaque étape = une branche = une PR, avec la sortie exacte de `pytest` et ses limites.
- Décisions actées : 6 schémas ; MPL-2.0 accepté (`certifi`, `orjson`, `tqdm`, dépendances indirectes) ; aucun doublon de champ dans les contrats.

## 5. Erreurs reconnues (traçabilité)

- Arena avait écrit `allowed_tools` au lieu de `allowed-tools` (spécification) → corrigé (`71d2722`).
- Arena avait contredit OpenHands à tort sur les étoiles de LiteLLM (le CSV dit 60057 ; 60043 venait de la v0).
- OpenHands a d'abord travaillé sur une référence périmée (`main` non fetché), puis l'a corrigé.
