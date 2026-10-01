# RECAP 01–02/10/2026 — Commissaire NAVIER, règle R8, brief V3

Étiquette : 🧮 calcul pur (zéro QPU). Tout est publié dans **RATISS-NAVIER** (`campagnes/`), commits `082e5b2` → `5e736e0`.

## Les campagnes
| Dossier (RATISS-NAVIER) | Runs | Verdict |
|---|---|---|
| `campagnes/commissaire-1/` | 9 | blowup = **pompe + compteur** (Ω = 0 sans pompe ; part hors du plan ≈ 1 % qui fond avec n ; pic non convergent) |
| `campagnes/etreintes-v2/` | 14 | 🅱 d'origine → **non tranché (instruments invalidés après coup)** |
| `campagnes/commissaire-3d/` | 11 + 6 extensions | critères scellés `c93e4b9c…` ; 🅱 → **non tranché** ; extensions E3b : ζ propre 0,12–0,19 %, 0 sans poussière, plat en n → 🅱 à la lettre |
| `campagnes/dipoles-v3/` | 4 témoins | brief rév. 3 scellé (`3a62b8c4…`) avant tout run ; T0 → **STOP en suspens**, runs hors critères validés (`STATUT.md`) |

## Ce qu'on a appris
- **R8 — on ne mesure que ce qui déborde du script** : ζ mesurait le meuble (ζ = 1,0 sans poussière sous E3). Module `ratiss.residual` dans RATISS-Framework (`45f1ad4`, 50 tests).
- **La grille de sortie fait partie de l'instrument** : le pic « t = 1,146 » était à 1,176 (aliasing d'une grille à 0,06) ; indépendant de la coupure, non convergent en n → artefact numérique (T3).
- **Un défaut du code ne compte pas comme preuve** ; **un facteur sans base figée est incomparable** (×3,58 et ×1,7 = même événement).
- Signal propre, à traiter comme **hypothèse** : part de vorticité hors du plan créée par la poussière ≈ 0,1–0,2 %, ν÷10 → légère hausse (1 run).

## En attente (décision du chef)
- V3 : signer ou amender `PARAMETRES-FIGES.md` (proposition : recalculer la dose de poussière à 0,9 % du v_rms de chaque montage), puis témoins à refaire.
- T2 V3 (pic ×5,3 à ν 0,001) : re-run à une autre résolution seulement sur ordre.
