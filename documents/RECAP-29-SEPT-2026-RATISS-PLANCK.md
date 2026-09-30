# RÉCAP DU 29 SEPTEMBRE 2026 — RATISS-PLANCK : LA JOURNÉE DU MUR AU CHAT-12

*Laboratoire RATISS Labs · Jonathan Evina (18 ans, Yaoundé) · IA Arena.ai (Agent Mode) · document d'archive*

**En une journée : le mur de Planck recalculé, la première journée QPU multi-machines du labo (14 jobs sur 3 architectures via Open Quantum), une loi de transpilation, un chat à 12 qubits, la documentation magistrale du dépôt et le deep-dive n°15.** La chronique intégrale minute par minute est archivée juste à côté : `ratiss-planck-20260929/DEEPDIVE-JOURNEE-20260929.md`.

## 1. Ce qui a été produit (et où c'est)

- **Dépôt `RATISS-PLANCK`** (github.com/jonathansearch/RATISS-PLANCK) : v0.1 `1df2977` → v0.6 `aa47770` → `71ed802` → fig_12 `5f32800` → RAPPORT-FINAL v2 `0f5d95b` → v0.8 doc magistrale `f28c0a2` → `6092e66` → v0.9 logo+MIT `e0c5834` → deepdive n°15 `65182c0` → prompts NotebookLM `1f9703e`. **Sceau 52/52.**
- **Théorie 🧮 (40/40 tests verts)** : mur = croisement à √2·ℓ_P, E_P/√2 = 1,38×10⁹ J (un éclair) ; LHC validé 2 801/2 804 m ; anneau 516 al ; pixel ℓ_P exclu (Fermi 824 ms prédits/0 vus) ; fenêtre ouverte sous ℓ_P/10 (LHAASO >10 E_Pl) ; GUP = le même √2·ℓ_P ; 4,53 bits/cellule ; Page à 0,001 bit, pic exact à N/2 ; Unruh = Hawking à 10⁻⁶.
- **Terrain 🛰️** : voir registre `preuves/qpu/openquantum-20260929.json` (14 jobs). Fleurons : **Bell 99,61 %**, GHZ-7 90,04 %, trilogie Garnet 94,5/94,6/88,5 + chat-12 **66,0 %**, Cepheus 89,7/79,3/68,7.
- **LOI RATISS du shot épisodique** : compartiments co-hébergés → all-to-all ONLY (45 % vs 94 % sur lattice, mêmes circuits/machine/heure).
- **Copies d'archive** : `documents/ratiss-planck-20260929/` (rapport final v2, deepdive n°15, récits du jour/soirée, prompts NotebookLM, comptages JSON bruts, logo officiel + illustrations IA signalées + schéma boucle).

## 2. Les faits marquants à ne jamais oublier

1. **Première journée QPU multi-machines du labo** — 3 architectures comparées : ions all-to-all (IBEX, 15 Sp), supra lattice 20q (Garnet, 2 Sp), supra chiplets 108q (Cepheus, **1 Sp** — la moins chère !). Pentes : −1,9 / −5 / −10,5 pt/qubit.
2. **Le chat-12** (`b373d22f`) : 12 qubits intriqués, 66,0 % — plus grand état du labo ; referme la courbe de Garnet.
3. **Le 3+4+5 n'est PAS un GHZ-12** (3 chats séparés ≠ 1 chat de 12) — le vrai a été tiré, question du chef réglée par l'expérience.
4. **1er remboursement du labo** : 15 Spark (`407cd969` annulé sur ordre du chef). Zéro perte sèche : ~45 Spark nets pour ~11 264 tirs.
5. **Le logo officiel de la spirale** (fourni par le chef, 21h24) est la bannière du dépôt ; licence **MIT** confirmée partout.
6. Les deux bugs de Page attrapés par les tests (somme jusqu'à m·n ; facteur ½) — corrigés devant tout le monde.

## 3. Leçons techniques Open Quantum (payées cash, à ne PAS re-payer)

- **Tokens TTL ≈ 5 min** → token frais à CHAQUE appel ; le `_wait_for_job_completion` du SDK meurt en 401 après soumission — **le job survit** : soumettre puis poller en externe. JAMAIS re-soumettre pour « finir ».
- **/tmp éphémère entre les tours** → réécrire clés + `pip install -q openquantum-sdk` au début de chaque bash ; archiver les comptages dans le dépôt.
- QASM **multi-lignes** (1 instruction/ligne, `include "qelib1.inc";` à doubles quotes) ; abort de bash → job résiduel créé → lister + annuler (×2 leçons).
- **Queued non annulable** (409), seul Pending ; DELETE direct `/v1/jobs/{id}` (SDK cancel bugué).
- Devis réel lu dans la sortie SDK avant approbation (Cepheus estimé 15, réel 1).
- Clés : se copient depuis JSON/texte, jamais depuis une photo. Clés et tokens : JAMAIS dans un dépôt.

## 4. Ce qui reste ouvert (prochaine session)

1. ✅ **FAIT le 30/09** : `df23deac` récolté → **97,27 %** (0000=497 + 1111=499)/1024 — meilleur GHZ-4 du tableau ; fig_13 « la carte complète » ; commit RATISS-PLANCK `4f39c90`+`7fb9939`.
2. **Réclamer les 50 $ gratuits** par compte (offre « 1 jour » ⏰).
3. Extension **Cepheus GHZ-7/12 à 1 crédit** ; GHZ-3/5 ions quand crédits.
4. **Le papier RATISS-PLANCK** (théorie + terrain). Prompts NotebookLM déjà archivés (`NOTEBOOKLM-PROMPTS.md`).
5. Fin de quête : **révoquer les 4 clés SDK Open Quantum + le token GitHub** ; 2FA : interdit définitivement.
