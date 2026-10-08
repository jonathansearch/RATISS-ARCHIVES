# 🧠 RÉCAP 08/10/2026 — RATISS-ONE DIALOGUES (leçons 38-40) + BASES-DONNÉES

Dépôts : https://github.com/jonathansearch/RATISS-ONE
https://github.com/jonathansearch/bases-donnees
Agent : Ratiss (Arena). Méthode : école manuelle (main d'abord, preuves exigées).

## 1. Dépôt `bases-donnees` créé (catalogue 16 sources)

| Contenu | Détail |
|---|---|
| Catalogue | 7 conversations + 9 français, fiches + échantillons ≤ 3 Mo |
| Listes | `LISTE-RESTE.md` (16 datasets, sources + commandes), `INDICE.md` (état) |
| Scripts | `echantillonner_s1.py`, `sonder_s2.py`, `ajouter_s2.py` (autre agent) |
| Loi | 1 dataset complet à la fois, brut jeté après usage (re-clonable en minutes) |

Tailles mesurées : discord 331 Mo, yield 363 Mo (105 735 blocs), ko-agent
1,36 Go, lmsys 1,49 Go, ultrachat 1,62 Go, escorpius 2,98 Go, wildchat
3,36 Go, CFDD ~15 Go (API HF). Léger : accueil 745 Ko, ding 1,2 Mo, cefr 722 Ko.

## 2. Les 3 leçons (dialogues_avérés → cerveau)

| Leçon | Dataset | Tours/mots | Fragment | Cerveau (+N/+L) | Batterie |
|---|---|---|---|---|---|
| 38 | accueil-ubs (41 dial.) | 1 062 / 6 295 | 3 072 liens | +101 / +2 166 | 127/127 |
| 38bis | accueil rejoué ×3 | — | +0 (100 %) | réservoir vide ✅ | 127/127 |
| 39 | ding-01 (10 dial.) | 14 834 / 70 274 | 17 705 liens | +536 / +12 102 | 128/128 |
| 40 | french_CEFR (6 000 phr.) | 6 000 / 109 486 | 53 828 liens | +5 571 / +38 332 | 129/129 |

Cerveau : 25 171/159 288 → **31 374/211 888** (+6 203 neurones, +52 600
liens), 36 motifs (MSUITE, MREPONSE, MA1..MC2), écoutes 300 000 000 (R5 intacte).
Motifs : MSUITE=12 789, MA1=1 061, MA2=1 506, MB1=2 245, MB2=3 753,
MC1=4 675, MC2=5 827. Chaque dataset rejoué ×3 (+0, signature identique).

## 3. Convertisseur dialogues v1→v3 (`education-manuelle/`)

- Formats : Accueil `X:`, Ding `NNNN L` (+horaires ignorés), phrases CSV
  (1 phrase = 1 dialogue, motifs de niveau MA1..MC2).
- Règles (documentées, pinnées) : `[crochets]` jetés, `(coupés-)` tombés,
  `(chevauchements)` gardés, `xxx` décollé + coupure, chiffres tombés,
  bruits chassés aussi accentués, pas de paire entre phrases isolées.
- Élisions résolues (leçon 40) : qu→que, c→ce, d→de, j→je, m→me, n→ne,
  s→se, t→te (+3 643 mots) ; `l'` coupé (ambigu).
- Bruits repérés MAIN : 46 (accueil) + 45 (ding) + 89 (cefr, chasse
  systématique : courts, triples, découpes + jugement). Zéro bruit résiduel
  vérifié à chaque leçon. On garde ce qui est vraiment dit (oral, franglais
  d'usage, noms propres, sigles) ; on jette transcripteur et collés.
- Fix batterie : OOM (tuée 2×) réparée en libérant les cerveaux (`del`).

## 4. Passerelle GLM

Méthode complète transmise (13 pas + code + lois + reste à boire) :
`education-manuelle/METHODE-DATASETS.md` (RATISS-ONE). Prochaine leçon = 41.

## 5. Blocages constatés (faits, non résolus)

| Source | Blocage |
|---|---|
| lmsys-chat-1m | gated HF (401, 1 clic requis) |
| CFDD / Claire | 401 HF (~15 Go) |
| iRead4Skills dataset 1 | accès restreint (lexiques 544 Ko publics) |
| FLEURON, TCOF | pages 404 (masses à retrouver) |
| french_CEFR | licence non indiquée (trace seule, texte jamais redistribué) |
| Corpus EN/ES | cerveau FR : décision du chef requise avant usage |

## 6. Commits du jour

RATISS-ONE : `2dc3312` (l38), `fb2f217` (38bis), `1fea704` (l39),
`8f5b9a2` (l40), `0ea94d5` + `2b42cc1` (passerelle GLM).
bases-donnees : `504014b` (init), `db504cf` (autre agent : catalogue FR),
`99d6697` (fix ko-agent), `08ff1bd`, `cfb81e9`, `8a9f994`, `a95e988` (3 bus).

Espace (chez Ratiss, workspace 128 Mo) : 117 Mo en fin de journée.
