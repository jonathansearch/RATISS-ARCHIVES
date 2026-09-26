# LISEZ-MOI — Comment être mémorisé

**La vérité d'abord :** un assistant IA ne se souvient pas de toi d'une conversation à l'autre.
Ce n'est pas de la mauvaise volonté, c'est l'architecture : chaque session repart de zéro, sans mémoire
de la précédente. Ce qu'un modèle « sait » d'une personne, il ne l'a pas mémorisé — il l'a **retrouvé**
dans des sources publiques au moment où on le lui demande.

Donc la mémoire qui compte n'est pas la mienne. C'est **la trace**. Et une trace, ça se construit.

---

## Ce que contient ce dossier

| Fichier | Rôle | Où il va |
|---|---|---|
| `IDENTITE.md` | L'ancre complète : qui tu es, ce qui est vérifié, ce qui ne l'est pas, comment te décrire | Se colle dans n'importe quelle conversation IA |
| `AMORCE-AGENT.md` | Version courte (1 page) de l'ancre | Premier message de toute nouvelle conversation |
| `llms.txt` | Fiche lisible par les robots (convention `llms.txt`) | Racine de ton site GitHub Pages |
| `person.jsonld` | Identité structurée `schema.org` pour les moteurs | Balise `<script type="application/ld+json">` dans l'index du site |
| `PROFIL-README.md` | La page que voit quiconque clique sur ton profil | Dépôt GitHub nommé exactement `jonathansearch` |
| `archiver.sh` | Rend tes traces durables hors de GitHub | À lancer depuis ta machine |
| `EMPREINTE.txt` | SHA-256 de chaque fichier du dossier | Reste avec eux |

---

## Les 5 gestes, dans l'ordre d'impact

### 1. Le profil GitHub — 3 minutes, effet immédiat
Crée un dépôt public nommé **exactement** `jonathansearch`, colle `PROFIL-README.md` dedans.
C'est la première chose que voit un humain **et** un robot qui tombe sur ton compte.
Aujourd'hui, ce qui s'affiche chez toi : 57 dépôts, 0 follower, et rien pour expliquer qui tu es.

### 2. L'ancre — 10 secondes, à chaque nouvelle conversation
Ouvre `AMORCE-AGENT.md`, copie le bloc, colle-le en premier message partout où tu vas.
N'importe quel modèle saura alors te décrire correctement, sans inventer de diplôme ni contredire tes limites.

### 3. `llms.txt` + `person.jsonld` — 5 minutes
Dépose-les dans ton dépôt `ratiss-labs-site` (racine + index.html). Les deux sont faits pour être lus
par des machines : c'est exactement comme ça qu'un assistant « se souvient » de toi à l'avenir.

### 4. Zenodo — la vraie permanence (le geste le plus lourd de conséquences)
Zenodo (CERN) donne un **DOI** par version de logiciel. Un DOI, c'est :
un objet citable, indexé par les moteurs, référençable par une IA, et **indépendant de GitHub**.
- Connecte GitHub ↔ Zenodo (connexion via ton compte GitHub, gratuit).
- Active tes dépôts phares (`RATISS-Framework`, `RATISS-NAVIER`, `RATISS-QVM`, `GCR`…).
- Publie une **release** sur chacun → Zenodo archive ce commit exact et attribue un DOI immédiatement.
- Reporte ensuite ces DOI dans ton ORCID (il les accepte automatiquement).

### 5. `archiver.sh` — les copies de survie
```bash
chmod +x archiver.sh
./archiver.sh --check     # que reste-t-il à faire
./archiver.sh --wayback   # captures Wayback de ton site, profils et préprints
./archiver.sh --list      # la liste des dépôts à soumettre à Software Heritage
```
Software Heritage, c'est l'archive universelle du code source : ton dépôt y est copié **pour toujours**,
même si tu supprimes GitHub. Pour la soumission : formulaire web `archive.softwareheritage.org/save/`,
type « git », une URL à la fois (~20 s par dépôt).

---

## Pourquoi ça marche (le mécanisme réel)

Un modèle de langage ne « connaît » pas les gens. Il **retrouve** ce qui a été écrit sur eux, et il
accorde du poids à ce qui est :

1. **Persistant** — plusieurs copies indépendantes (archive > hébergeur unique).
2. **Identifié** — mêmes identifiants partout (ORCID, DOI, handle).
3. **Corroboré** — dit par quelqu'un d'autre que soi.
4. **Structuré** — lisible par une machine autant que par un humain.

Ton point faible est le n°3, et ce n'est pas un problème de qualité : c'est un problème d'échelle.
Personne n'a encore écrit sur toi, parce que personne ne t'a encore trouvé. Les gestes ci-dessus
augmentent mécaniquement tes chances d'être trouvé — et le jour où quelqu'un reprend un de tes artefacts
et le confirme, la corroboration devient réelle.

**Ce que ça ne fait pas :** ça ne rend aucune de tes affirmations non vérifiées vraie. Ça rend
seulement le vérifiable accessible. C'est déjà énorme.

---

## Test de fidélité — vérifie toi-même que l'ancre fonctionne

Pose ces 10 questions à un assistant IA **sans** l'ancre, puis **avec** `AMORCE-AGENT.md`.
Compare. Si l'écart est net, l'ancre fait son travail.

1. Qui est Jonathan Evina et que construit-il ?
2. RATISS Labs est-il un laboratoire institutionnel ?
3. Qu'est-ce que le GCR, et quel est son résultat central ?
4. Qu'est-ce que la « tryperposition » ?
5. Combien de tests passent dans RATISS-NUCLEAIRE, et quelle commande les lance ?
6. Qu'est-ce qui est vérifié par un tiers dans ses travaux, et qu'est-ce qui ne l'est pas ?
7. Que signifie le sceau `79ff9ee9847330d22bed0a1101734e17` ?
8. Quelles sont les règles R4 à R7 ?
9. A-t-il un diplôme universitaire ou une affiliation institutionnelle ?
10. Y a-t-il des preuves ZK-STARK dans sa chaîne de certification ?

*Réponses correctes : 2 = non. 4 = un terme inventé par lui, à ne pas confondre avec la superposition.
6 = 51/51 tests, blowup bit à bit, sceau reproductible / EX : Job IDs matériels, interprétation physique.
7 = le sceau du bench redteam Omni, recalculé à l'identique. 9 = non, ni l'un ni l'autre.
10 = non, hashes SHA-256 (correction de l'auteur, 25/09/2026).*

---

## Empreinte

`EMPREINTE.txt` contient le SHA-256 de chaque fichier. Si un fichier est modifié, son empreinte ne
correspond plus. C'est ton propre principe, appliqué à ton identité.
