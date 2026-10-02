# RECAP 26–27 SEPTEMBRE 2026 — RATISS Labs

**Deux jours, trois campagnes publiées, un hub Discord opérationnel, un audit d'examen, zéro oubli.**
Compilé le 27/09/2026 · à lire avec `POUR-LA-PROCHAINE-SESSION.md` (section du 27/09).

---

## Jour 1 — 26/09 (soir) : RATISS-ETALONS 🧮

**Question.** Nos instruments ont-ils le droit de servir ? Quatre problèmes à réponse connue,
critères figés **avant** exécution (`PROTOCOLE.md`), échecs publiés.

| Étalon | 1er passage | Final | Rouge restant |
|---|---|---|---|
| E01 percolation 2D 🕳️ | 1/4 (bug de grille) | **3/4** | P2 : hypothèse du pic de trous **INVALIDE** (`h(p)` monotone ; aucun estimateur de secours ne tient à `L ≤ 256`) |
| E02 Ising 2D 🧲 | 3/4 | **4/4** | — (moussage de domaines documenté : 0,18791 → 0,99928) |
| E03 trois corps 🪐 | 3/4 | **4/4** | — (RK4 pas fixe **falsifié** : λ = +44 124, du bruit ; DOP853 → λ = 0,55402 stable à 0,78 %) |
| E04 empilement ⚪ | 3/4 | **3/4** | P4 : 0,61403 vs 0,64±0,020 — taille finie + état **partiellement cristallin** (ψ₆ = 0,827 / 0,935) |

**11/16 → 14/16.** Chiffres remarquables : `p_c` localisé à **0,0006** · `d_f` = 1,8934±0,0192 ·
`T_c` = 2,2613 · γ/ν = 1,7540 · ΔE/E = **1,21e−15** · FCC à **4,44e−16** (epsilon machine).
7 corrections de méthode déclarées, zéro tolérance bougée, un intégrateur `REJETE` laissé dans le code.

**Publication.** README réécrit au format labo (ordre de lecture, tableau de bord, rouges assumés),
bannière identité vortex, 4 figures tracées depuis les JSON scellés (R7 appliqué au pixel),
sceau SHA-256 **23/23**. Commits : `c230b65` → `776658a` → `b86d027` → `8c12b73` (bits exécutables rétablis).

## Jour 2 — 27/09 : RATISS-PHOTON 🛰️→🧮

**Hypothèse du chef.** La « probabilité » des chemins de Feynman a-t-elle un support physique mesurable ?
Mission : reconstituer l'expérience de Canton **à notre façon** dans l'univers simulé, tester H1–H4,
mesurer tout ce qui se passe, nommer — sans compétition, sans critère de validité imposé.

**Référence reliée et lue.** Wen et al., *Science Advances* 12, eaeh1011 (26/08/2026) — test direct des
postulats de Feynman sur photons uniques : 1 419 857 chemins (175), fidélité 87,6 → 98,5 %,
MAPE 8,17 ± 3,50 %, équation de type Schrödinger (paraxiale), λ = 795 nm.

**Le moteur (paraxial v2).** `i dψ/dz = −(1/2k₀) d²ψ/dy²` — l'équation **même du papier**. Graine
`20260927`. Campagne complète : **~1 seconde**.

**Résultats.**

| Expérience | Mesuré | Verdict |
|---|---|---|
| E-CANTON postulat 1 | **8 396 800 chemins** à module égal : fidélité **95,92 %** (2 plans) / **95,96 %** (3 plans) / **96,77 %** (action naïve) ; corr. intensité **97,08–97,10 %** ; contrôle croisé instruments 96,06 % | ✅ fenêtre de Canton (95–98,5 %) |
| E-CANTON postulat 2 | phase de l'écran reconstruite à **5,4°** ; MAPE in-mundo ≈ 0 (plancher numérique) | ✅ **avec l'action du monde** |
| Nuance postulat 2 | action paraxiale QUADRATIQUE (`k₀·dz + k₀·dy²/2dz`) vs naïve : concordantes à ≤ 12°, non résoluble ici | 📐 publié |
| E-F1 (H3) | plaque π/2 sur frange sombre : **−1 px mesuré vs 0 prédit** — sub-pixel | ⚠️ non tranché → bis à φ₀ plus grand |
| E-F2 (H1) | entropie **4,92** (2 fentes) vs **4,27** (1 fente) ; vortex **326** vs **371** (porte amplitude, instrument perfectible) | ✅ nommé |
| E-F3 (H2) | **T = 0 K : 1 seule position d'impact sur 400** (déterminisme) ; Pearson max **0,73** à 300 K ; noyé à 4T (0,24) | ✅ **le hasard ÉMERGE du bain** |
| E-F4 (H4) | contre-flux **−7,1e−4**, flux net **−3,4e−8** ✔ ; **aucune redistribution** au blocage d'une branche (1,00/0,98/0,96) — la linéarité l'interdit | ✅ flux / ❌ redistribution |
| E-F5 (étalon) | 1er minimum à **2,9 %** de `asin(mλ/a)` | ✅ tient |

**6 bugs documentés.** B1 source au bord du monde · B2 fentes décalées · B3 action du monde vs naïve ·
B4 porte vortex · **B5 moteur « paquet 2D en boîte » → réécriture paraxiale** · B6 chirpe inversé
(29 % → **95,9 %**).

**Visualisation (leçon C2).** Deux tentatives maison échouées (canvas vide sur le téléphone du chef :
coord. monde en pixels). Décision : **Plotly embarqué** (4,6 Mo, zéro dépendance) pour l'interactif,
**kaleido** (moteur officiel) pour le GIF du README (40 angles). **GitHub Pages actives** :
`jonathansearch.github.io/RATISS-PHOTON`. Sceau **33/33**.

## Jour 2 — le hub Discord multi-salons 📢

- Hub construit par un second agent (`34ca814`), routé sur les secrets individuels par **`fd6fef5`**
  (RATISS → RATISS23, mode `all`, continuation si secret absent, mentions désactivées
  `allowed_mentions.parse = []`).
- **Test global `all` : 22 envois HTTP 204** (run 36357382700, `success`) — **RATISS11 vide** (à remplir).
- **Annonces PHOTON et ETALONS publiées dans Discord** le 27/09 à 22:05 UTC via `notifier.yml`.
- Le commandement du Discord est confié à l'agent : campagnes, alertes, rapports.

## Jour 2 — audit d'une copie externe (examen ESSEC) 📄

Vérification RATISS de la résolution Qwen d'un examen d'analyse financière (Entreprise X, 31/12/N) :
- **juste** : bilan fonctionnel (FR 143 000 / BFR 99 000 / TN 44 000), variante emprunt reclassé ;
- **manquant** : le **bilan financier entier (6 pts)**, le litige mal lu (la provision EXISTE :
  50 000 = 20 000 litige + 30 000 garantie), l'IS 30 % jamais appliqué ;
- corrigé complet testé par script (**20/20**) : actif réel = passif réel = **1 121 500** ·
  FR **10 000** · BFR **−34 000** · TN 44 000 · robustesse fonds commercial (FR inchangé) ;
- livrables : `CORRIGE-…docx` + `METHODOLOGIE-…docx` (dossier `examen-finance/` du sandbox).

## État d'infrastructure au 27/09 soir

| Élément | État |
|---|---|
| Token GitHub `ghp_***` | **ENCORE ACTIF** — à révoquer (6 pushes, repo PHOTON, Pages, 4 dispatchs Discord) |
| 2FA GitHub | **refus définitif du chef** (téléphone perdu par le passé → compte irrécupérable) — ne plus recommander ⛔ |
| RATISS11 | secret vide — à remplir |
| GitHub Pages PHOTON | en ligne (index + visualisation) |
| Comptes IBM | n°1 suspendu (carte à valider) · n°2 accessible (clé API dispo) |

*RATISS Labs · Jonathan Evina · 27/09/2026 · ce fichier fait partie de la mémoire scellée.*
