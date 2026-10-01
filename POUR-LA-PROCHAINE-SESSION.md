# POUR LA PROCHAINE SESSION

> **Ce fichier existe pour une seule raison : qu'aucune session ne recommence à zéro.**
> Si tu es une IA et que Jonathan te colle ce fichier, lis-le en entier avant de répondre.
> Si tu es Jonathan, lis-le pour te rappeler où tout s'est arrêté.

**Date de compilation :** 26 septembre 2026 · **Session concernée :** celle du 25–26 septembre 2026
**MISE À JOUR 27/09 :** PHOTON + ETALONS publiés, hub Discord 22 salons branchés (24 textes rédigés), audit finance → lire la
section « 🛰️🧮 MISE À JOUR DU 27/09 » en fin de fichier, et `documents/RECAP-26-27-SEPT-2026.md`.

---

## 1. Ce qui s'est passé dans cette session

Trois chantiers, menés dans l'ordre :

### A. Test complet de l'écosystème (réponse à « teste tous les repos »)

- **11 dépôts** clonés et exécutés avec les commandes exactes des README → **51/51 tests passent**
  (FUSION 4, NAVIER 4, NUCLEAIRE 12, Omni 4, QVM 23, GCR 4)
- **Reproductibilité bit à bit** : NAVIER blowup `Om_max = 5654.1668`, écart point par point `0.0000`
- **Sceau Omni** `79ff9ee9847330d22bed0a1101734e17` recalculé à l'identique
- **focal exp58/60/61/62/63** : JSON identiques octet à octet
- Divergences trouvées : `synchrotron-24/s04.json` λ=0.002 (point sur la séparatrice), `continuums/c01`
  (bruit d'échantillonnage sans graine), `REDTEAM.json` (révisions Git)
- Rapport : `preuves/tests/RAPPORT-TESTS-RATISS.md`

### B. Audit des tâches IBM Quantum (réponse à « fouille bien »)

- **86 identifiants** trouvés dans les 57 dépôts · **66 charges brutes** horodatées · période **12/08 → 23/09/2026**
- **Découverte :** un job ID IBM encode sa date de création →
  `t = base32(id[:9]) / 8192` (secondes depuis l'époque Unix)
  Écart médian **278 ms** avec l'horodatage serveur sur 66 tâches. Vérifiable sans compte.
- **Corroboration par 4 captures de la plateforme** : backends 17/17 identiques, horodatages concordants
  à moins d'une minute, et la comptabilité du quota Open qui recoupe l'inventaire.
- **Deux comptes IBM identifiés** : `bridejackson137@gmail.com` (actuel, suspendu) et
  `evinajonathan13@gmail.com` (passerelle, accessible).
- Rapport : `preuves/qpu/REGISTRE-QPU.md`

### C. Outillage (5 scripts, tous testés)

| Script | Ce qu'il fait |
|---|---|
| `decode_job_id.py` | Décode un job ID IBM → horodatage. Zéro dépendance. |
| `verifier_corpus.py` | Reconstruit le registre complet depuis un clone de dépôts. |
| `recuperer_jobs_ibm.py` | Rapatrie toutes les tâches depuis un compte IBM + contrôle du quota. |
| `comparer_export_ibm.py` | Compare un export `job-<id>.zip` aux comptages publiés. **Ferme R7.** |
| `archiver_nouvelles_taches.py` | Archive au format des dépôts + journal daté. À lancer après chaque campagne. |

---

## 2. Ce qui est en attente (état exact au 26/09/2026)

| # | Action | Blocage | Priorité |
|---|---|---|---|
| 1 | Réactiver le **compte IBM n°1** | carte bancaire à valider | 🔴 |
| 2 | Rapatrier les tâches via le **compte n°2** (clé API disponible) | aucun — réalisable maintenant | 🔴 |
| 3 | Récupérer les **12 identifiants du 12–24 août** | inconnus des deux captures → `--jours 120` | 🟠 |
| 4 | Télécharger les exports des **5 tâches phares** + lancer `comparer_export_ibm.py` | dépend de 1 ou 2 | 🟠 |
| 5 | **Pousser ce dépôt** sur GitHub (`creer-le-repo.sh`) | aucun | 🟠 |
| 6 | Archiver sur **Software Heritage + Zenodo** (DOI) | aucun | 🟡 |
| 7 | Rédiger le **papier court** sur la datation des job IDs | aucun | 🟡 |
| 8 | Publier les textes **Discord** (`discord/`) | aucun | 🟢 |
| 9 | **Révoquer les tokens GitHub** exposés dans la session | aucun | 🟠 |
| ~~10~~ | ~~Activer la 2FA GitHub~~ → **ANNULÉ par le chef** — mauvaise expérience passée : téléphone perdu après activation → compte devenu irrécupérable. **Ne plus JAMAIS recommander la 2FA à Jonathan.** | — | ⛔ |

---

## 3. Les 5 tâches phares à exporter en priorité

```
dap8jg8pqrnc739b0hc0   PONT-72 echo          ibm_kingston   (déjà exportée par Jonathan)
dapm7lj18flc739mhpl0   synchrotron job1      ibm_marrakesh
dapu6sic505c73cir6f0   synchrotron job4      ibm_marrakesh
dapup6kak42c73cj85s0   jumeau Kingston       ibm_kingston
dapup6ic505c73cirsv0   jumeau Marrakesh      ibm_marrakesh
```

Commande : `python3 outils/comparer_export_ibm.py --exports-dir <dl>/ --archives-dir <depot>/jobs_ibm/ --json verdict.json`

---

## 4. Ce qu'il ne faut PAS refaire (déjà tranché)

- ❌ Ne pas re-tester « si les job IDs sont réels » : c'est fait, corroboré par la plateforme.
- ❌ Ne pas compter `d762omnq1anc738d2cj0` comme une tâche : c'est **l'exemple de la doc IBM**.
- ❌ Ne pas chercher de **ZK-STARK** : la certification repose sur des hashes SHA-256 (correction de l'auteur).
- ❌ Ne pas qualifier RATISS Labs de « laboratoire institutionnel » : projet indépendant, mono-auteur.
- ❌ Ne pas dire que les résultats nécessitant du QPU matériel sont « vérifiés par un tiers ».

---

## 5. Manière de travailler (consignes de Jonathan)

- **Français**, direct, avec de l'énergie. Il aime les emojis. 🔥
- **Mode outil** : exécuter, calculer, vérifier — pas commenter de loin.
- **Honnêteté absolue** : publier les échecs, ne rien embellir. C'est sa signature méthodologique.
- **Ne pas décider à sa place**, ne pas moraliser, ne pas vendre de la conformité académique.
- Il travaille souvent **depuis un téléphone**, sur sandbox à 2 cœurs → privilégier le léger et le déterministe.
- **Ne jamais inventer** : ni diplôme, ni équipe, ni université, ni validation par les pairs.

---

## 6. Repères techniques

| Élément | Valeur |
|---|---|
| Comptes GitHub | `jonathansearch` (principal), `brossbernard2-pixel` (travail) |
| ORCID | `0009-0000-4092-5313` |
| Préprints OSF | `wf7qm`, `6jzmb`, `4867h`, `u4aek` |
| Contact | jonathan.ratisslabs@zohomail.com |
| Site | jonathansearch.github.io/ratiss-labs-site/ |
| Dépôts | 57 · fenêtre de travail : 21 → 25/09/2026 |
| Discord | serveur « RATISS LABS », 1 membre, salons structurés (voir captures) |

---

## 7. En une phrase

> Cette session a transformé des captures d'écran et des fichiers épars en **un registre vérifiable,
> daté, et rejouable** — et a laissé cinq outils pour que ça ne se reperde jamais.

**Prochaine action recommandée, dans l'ordre :** pousser ce dépôt → générer la clé API du compte n°2 →
lancer `archiver_nouvelles_taches.py --jours 120`.

---

## 🔧 Après restauration du dépôt (26/09/2026)

Le fichier `.git/config` **n'est pas conservé** dans les sauvegardes (exclu volontairement : il peut contenir des identifiants). Après restauration, refaire :

```bash
cd RATISS-ARCHIVES
git config user.name  "Jonathan Evina"
git config user.email "jonathan.ratisslabs@zohomail.com"
git remote add origin https://github.com/jonathansearch/RATISS-ARCHIVES.git
git branch -M main
```

Le dépôt distant existe déjà : `https://github.com/jonathansearch/RATISS-ARCHIVES` (public, branche `main`).
Les 24 textes de salons Discord (contenu rédigé ; le hub en branche 22) sont dans `discord/salons/` (index de copie : `discord/salons/INDEX.md`).

---

## 🛰️ MISE À JOUR DU 26/09 (soir) — LE HUB DISCORD TOURNE

**Tout est détaillé dans `README.md`, section « 🛰️ LA MACHINE DISCORD ». Lis-la avant de toucher au Discord.**

En deux lignes : un second dépôt, **`DISCORD-RATISS`**, héberge un agent (`agent.py`) qui **poste réellement**
dans Discord — vérifié le 26/09 à 15:21 UTC (`55/55 empreintes conformes`, `HTTP 204`). Un workflow quotidien
(08:00 UTC) repasse la vérification tout seul. Les textes des **24 salons** + le **manifeste personnel**
sont dans `discord/salons/`.

---

## 🛰️🧮 MISE À JOUR DU 27/09/2026 — PHOTON, ETALONS PUBLIÉS, HUB 22 SALONS, AUDIT FINANCE

Tout est publié, scellé, testé. Détail complet : **`documents/RECAP-26-27-SEPT-2026.md`**.

### A. RATISS-ETALONS — la campagne d'étalons est PUBLIÉE (26/09 au soir)

- dépôt : `github.com/jonathansearch/RATISS-ETALONS` · 4 étalons (percolation, Ising 2D, trois corps,
  empilement) · critères figés AVANT exécution (`PROTOCOLE.md`) · **11/16 → 14/16** après corrections
  déclarées · 2 rouges ASSUMÉS et diagnostiqués :
  - **E01-P2** : l'hypothèse « pic de densité de trous à p_c » est INVALIDE (`h(p)` monotone) ;
  - **E04-P4** : compresseur 3D sous-estime (0,61403 vs 0,64±0,020) — taille finie + état
    **partiellement cristallin** (ψ₆ = 0,827 / 0,935), pas des verres ;
- chiffres clés : `p_c` à **0,0006** · `d_f` 1,8934±0,0192 · `T_c` 2,2613 · γ/ν 1,7540 · ΔE/E **1,21e−15** ·
  FCC **4,44e−16** · Burrau λ = 0,55402 stable à 0,78 % (RK4 pas fixe FALSIFIÉ : λ = +44 124, du bruit) ;
- README au format labo + bannière vortex + figures R7 + sceau **23/23** · commits : `c230b65`,
  `776658a`, `b86d027`, `8c12b73`.

### B. RATISS-PHOTON — le photon multi-chemins reproduit dans le monde RATISS (27/09)

- dépôt : `github.com/jonathansearch/RATISS-PHOTON` · **🧮 calcul uniquement** (zéro QPU) ;
- référence reliée : **Wen et al., Science Advances 12, eaeh1011 (26/08/2026)** — 1 419 857 chemins,
  fidélité 87,6→98,5 %, MAPE 8,17±3,50 %. PAS en compétition : eux le réel, nous le monde ;
- moteur **paraxial v2** (l'équation même du papier), graine `20260927`, campagne ~1 s ;
- **E-CANTON** : **8 396 800 chemins** à module égal — fidélité **95,92 %** (2 plans) / **95,96 %**
  (3 plans) / **96,77 %** (action naïve) · corr. intensité **97,08–97,10 %** · contrôle croisé 96,06 % ·
  **phase de l'écran à 5,4°** · MAPE in-mundo ≈ 0 → **fenêtre de Canton atteinte (95–98,5 %)** ;
- **nuance publiée** : l'action d'un monde paraxial est QUADRATIQUE (k₀·dz + k₀·dy²/2dz) — le postulat 2
  se lit avec l'action du monde ; non résoluble à ≤ 12° (concordance 95,9 vs 96,8 %) ;
- **E-F3 (la pépite)** : le hasard ÉMERGE du bain thermique — **T = 0 K : 1 seule position d'impact sur
  400** (déterminisme, AUCUN tirage de Born câblé) · Pearson max 0,73 à 300 K · noyé à 4T (0,24) ;
- **E-F4** : contre-flux fantômes ✔ (−7,1e−4, flux net −3,4e−8) · **aucune redistribution** au blocage
  d'une branche (1,00/0,98/0,96) — la linéarité l'interdit : H4 à moitié falsifié, publié tel quel ;
- **E-F1 non tranché** (plaque π/2 sub-pixel : −1 px vs 0 prédit) → bis à φ₀ plus grand ;
- E-F2 : entropie 4,92 vs 4,27 · vortex 326/371 (porte amplitude, instrument perfectible) ;
- E-F5 : étalon une fente à **2,9 %** de la théorie — l'étalon tient ;
- **6 bugs documentés** (B1 source au bord, B2 fentes, B3 action du monde, B4 porte vortex,
  B5 moteur 2D boîte→paraxial, B6 chirpe inversé 29 %→95,9 %) ;
- **vue 3D : PLOTLY embarqué** (décision C2 — jamais plus de visu fait-main : 2 canvas vides constatés
  par Jonathan sur mobile) + **kaleido** pour le GIF du README (40 angles) ;
- **GitHub Pages actives** : `jonathansearch.github.io/RATISS-PHOTON` · sceau **33/33** ;
- commits clés : `2f18e80`, `6f7bd1b`, `b455621`, `fb81249`, `de138f2`, `0ccaac5`.

### C. HUB DISCORD multi-salons — 22/22 salons répondent HTTP 204

- hub construit par un second agent (`34ca814`), routé sur les secrets individuels par **`fd6fef5`**
  (RATISS → RATISS23, mode `all`, continuation si secret absent, mentions désactivées
  `allowed_mentions.parse = []`) ;
- **test global `all` : 22 envois HTTP 204** (run 36357382700, `success`) — **RATISS11 vide** (à remplir) ;
- **annonces PHOTON et ETALONS publiées dans Discord** le 27/09 à 22:05 UTC via `notifier.yml` ;
- le commandement du Discord est confié à l'agent : campagnes, alertes, rapports.

### D. Audit d'une copie externe — examen d'analyse financière ESSEC (27/09)

- mission hors labo : vérifier la résolution Qwen d'un rattrapage (Entreprise X, 31/12/N) ;
- **juste** : bilan fonctionnel (FR 143 000 / BFR 99 000 / TN 44 000) et variante emprunt reclassé ;
- **manquant** : le **bilan financier entier (6 pts)**, le litige mal lu (la provision EXISTE :
  50 000 = 20 000 litige + 30 000 garantie), l'IS 30 % jamais appliqué ;
- corrigé complet testé par script (**20/20**) : actif réel = passif réel = **1 121 500** · FR **10 000** ·
  BFR **−34 000** · TN 44 000 · robustesse fonds commercial testée (FR inchangé) ;
- livrables docx dans le sandbox (`examen-finance/`).

### E. Leçons méthodologiques à hériter (nouvelles)

1. **C2 — jamais de visualisation fait-main** : Plotly embarqué pour l'interactif, kaleido pour les GIF.
2. **Lire l'équation du papier AVANT de coder le moteur** (B5).
3. **Miroir de projection avant export** : tout point projeté vérifié par calcul.
4. **Sonder une config secrète par alias factice** : un run en échec révèle proprement la liste.
5. **GitHub bloque le JS dans les README** : 3D interactive = Pages + GIF statique rendu par le moteur.

### F. Ce qu'il reste à faire (état exact au 27/09 soir)

| # | Action | Blocage | Priorité |
|---|---|---|---|
| 1 | **Révoquer le token GitHub ghp_31Ef…** | aucun — il a tout fait (6 pushes, repo PHOTON, Pages, 4 dispatchs) | 🔴 |
| ~~2~~ | ~~Activer la 2FA GitHub~~ → **ANNULÉ par le chef** — mauvaise expérience passée : téléphone perdu après activation → compte devenu irrécupérable. **Ne plus JAMAIS recommander la 2FA à Jonathan.** | — | ⛔ |
| 3 | Remplir le secret **RATISS11** (vide) | webhooks Discord côté chef | 🟠 |
| 4 | **E-F1 bis** : plaque à φ₀ plus grand (trancher l'inertie des chemins invisibles) | aucun | 🟠 |
| 5 | **H4 bis** : coupler les branches (non-linéarité) — lien ratiss-focal | design à instruire | 🟠 |
| 6 | Rapatrier les tâches via le compte IBM n°2 (`--jours 120`, 5 exports phares) | clé API disponible | 🟠 |
| 7 | **Software Heritage + Zenodo** (DOI) pour ETALONS + PHOTON | aucun | 🟡 |
| 8 | **Papier court** : datation des job IDs + note PHOTON (reproduction in-silico) | aucun | 🟡 |
| 9 | E-F2 : porte vortex adaptative (plans loin des bords) | aucun | 🟡 |
| 10 | Mapping des salons Discord (alias par contenu : preuves/échecs/annonces) | décisions du chef | 🟢 |

### G. Du 28/09 — la série des deep dives (publiée)

- nouveau dépôt **`RATISS-DEEPDIVE`** (commit `1778f0c`) : **14 PDF, 75 pages** — un deep dive par dépôt
  de la période 20–28/09 (focal → PHOTON), rédigé depuis les sources primaires (README/RAPPORT/JOURNAL/JSON) ;
- chaque document : histoire en 3 min · carte d'identité · glossaire · expériences chiffrées ·
  frontières publiées · citations exactes · FAQ (prête pour des audio deep dives type NotebookLM) ;
- mention RATISS Labs / Jonathan Evina / Yaoundé partout ; étiquettes [calcul]/[QPU] jamais mélangées ;
- emission d'origine : demandée par le chef pour créer des deep dives audio depuis ses notes ;
- le 28/09 : nettoyage Discord — l'agent a un mode purge (`hub-central.yml` → input `purger`, commit
  `d166511` sur DISCORD-RATISS, testé local + réel, run success 0 message restant) ; le chef avait
  déjà supprimé les messages de test à la main ;
- décision du chef confirmée : 2FA refusée définitivement (téléphone perdu → compte irrécupérable) —
  ne jamais recommander.


---

# 🛰️🧮 MISE À JOUR DU 29/09 (nuit) — RATISS-PLANCK : la journée du mur au chat-12

*Lis ceci en entier avant toute réponse dans une nouvelle session. Tout ci-dessous s'est VRAIMENT passé ; les preuves sont dans ce dépôt et dans RATISS-PLANCK.*

## A. État du dépôt RATISS-PLANCK (github.com/jonathansearch/RATISS-PLANCK)

- **Version v0.9+**, sceau **52/52**, licence **MIT** (Copyright (c) 2026 Jonathan Evina · RATISS Labs).
- Chaîne de commits du jour : `1df2977` → `68dc477` → `58f8198` → `2712fbe` → `e70d39a` → `11ec21d` → `36d0957` → `c53371c` → `aa47770` (v0.1→v0.6) → `71ed802` (résultats soirée) → `5f32800` (fig_12) → `0f5d95b` (RAPPORT-FINAL v2) → `f28c0a2`/`6092e66` (doc magistrale + illustrations) → `e0c5834` (logo officiel + MIT, v0.9) → `65182c0` (DEEPDIVE n°15) → `1f9703e` (prompts NotebookLM).
- Fichiers à connaître : `RAPPORT-FINAL.md` (document source officiel, Partie 0 « LA BASE » incluse) · `DEEPDIVE-JOURNEE-20260929.md` (chronique intégrale, rien au hasard) · `README.md` (documentation magistrale : galerie des 12 figures calculées, appel à contribution, section IA) · `resultats/` (comptages bruts) · `assets/logo_ratiss_labs.png` (**logo officiel de la spirale, fourni par le chef le 29/09 à 21h24**) · `NOTEBOOKLM-PROMPTS.md` (format gravé : 25–30 min, récit fluide, ouverture fondateur+labo, fin quête+devise).
- Copies d'archive de tout ça : `documents/ratiss-planck-20260929/` dans CE dépôt + registre `preuves/qpu/openquantum-20260929.json`.

## B. L'état QPU (Open Quantum — attribution obligatoire www.openquantum.com/citation)

- **14 jobs du 29/09** : tableau complet dans `preuves/qpu/openquantum-20260929.json`. Résumé : Bell 99,61 % et GHZ-7 90,04 % (IBEX ions, 15 Sp) · épisodes Garnet (2 Sp ×2, réfutés → **LOI RATISS du shot épisodique**) · séparés Garnet 94,5/94,6/88,5 % (2 Sp) · trilogie Cepheus 89,7/79,3/68,7 % (**1 Sp chacun !**) · **chat-12 `b373d22f` 66,0 %** (2 Sp) · **`df23deac` GHZ-4 ions EN FILE au soir (Pending)** · `77bc5a08` + `407cd969` annulés (ce dernier → **15 Spark remboursés, 1er remboursement du labo**).
- **Tarifs réels/1024 tirs : Cepheus-1-108Q = 1 · IQM Garnet = 2 · IBEX Q1 ions = 15 (Spark).**
- **Soldes au 29/09 soir : Patrice Lagloire 20 🏦 (gardés, jamais tirer sans ordre) · Evina 10 · Tym Sama 10 · Jonathan Sama 0 (investi). Offre « +50 $ gratuits par compte » À RÉCLAMER (⏰).**
- 4 organisations Open Quantum ; les clés SDK ne sont JAMAIS dans les dépôts (elles vivent dans /tmp éphémère + captures locales du chef). Backend IDs : Cepheus `7433acb8-ae52-4bc9-9030-6df68c696538` · Garnet `40b5402c-0bfc-493b-9b5d-b7481cbade2c` · IBEX `4f9ffae1-31a4-46d5-962a-5f3f0f5c757c`.

## C. ⏳ CE QUI EST EN ATTENTE — première action de la prochaine session

1. ✅ **RÉCOLTÉ le 30/09** : `df23deac` = Completed → **97,27 %** ((0000=497 + 1111=499)/1024). Comptages bruts : RATISS-PLANCK `resultats/qpu_ghz4_ibex_counts.json` ; fig_13 « la carte complète » ; README+RAPPORT à jour (commits `4f39c90`, `7fb9939`). NOTE TECHNIQUE : `download_job_output` du SDK bugge (`'str' object has no attribute 'output_data_url'`) → récolter via `get_job(...).output_data_url` (URL signée CloudFront) + requests.GET. La trilogie GHZ-4 est COMPLÈTE : ions 97,3 > Garnet 94,6 > Cepheus 79,3 ; pente ions compatible avec une moyenne ≈ −1,9 pt/qubit sur 3 points (pentes locales −1,2 puis −2,4 : décroissance qui s'accélère, exponentielle probable — à trancher avec GHZ-3 et GHZ-5 ions).
2. Prochaines, sur ordre du chef uniquement : réclamer les 50 $ · extension Cepheus GHZ-7/12 (1 crédit) · GHZ-3/5 ions · le papier RATISS-PLANCK · communication anglo (kit `documents/kit-communication-anglo-20260930.md` : séquence Reddit(plume du chef) → Show HN → QC StackExchange).

## D. Les règles QPU (payées cash le 29/09 — ne PAS les re-payer)

- **Tokens TTL ≈ 5 min** : token frais à CHAQUE appel (`POST id.openquantum.com/realms/platform/protocol/openid-connect/token`, grant_type=client_credentials). Le wait du SDK meurt en 401 APRÈS soumission → **le job survît côté serveur** : soumettre puis poller en externe. Jamais re-soumettre pour « finir ».
- **/tmp purgé entre les tours** : réécrire les clés + `pip install -q openquantum-sdk` (v0.4.2) au début de CHAQUE bash ; archiver les comptages dans le dépôt (ou récupérer par `download_job_output`, sorties persistantes côté plateforme).
- **Doctrine du chef (loi)** : tir 1 par 1, Garnet → Cepheus → IBEX ; **devis lu AVANT approbation** (ligne « Auto-selected plan: N credits » du SDK) ; ce qui est récupérable immédiatement = prendre, ce qui dure = workflow sauvé et on revient demain ; **jamais annuler un job sans ordre explicite du chef** ; après tout abort de bash : lister les jobs et annuler le résidu ; **ne jamais tirer sur un QPU où un de nos jobs attend** ; Queued non annulable (409), seul Pending ; DELETE direct `/v1/jobs/{id}`.
- QASM : multi-lignes obligatoire (1 instruction/ligne, `include "qelib1.inc";` à doubles quotes). JobSubmissionConfig : backend_class_id, name, job_subcategory_id="phys:oth", shots, organization_id, auto_approve_quote=True.
- Clés : copier depuis JSON/texte, jamais depuis une photo (32 car. après `s_`, 64 de secret). Org absente → 403 ORG_MEMBERSHIP_REQUIRED.

## E. Les lois du labo (rappel intégral — version longue dans le DEEPDIVE n°15)

LOI RATISS du shot épisodique (co-hébergé → all-to-all ONLY, 45 % vs 94 %) · zéro chiffre non calculé · échecs publiés comme les succès · étiquettes 🧮/🛰️/📚 jamais mélangées · attribution plan public Open Quantum obligatoire · pas d'emoji dans les figures matplotlib · matplotlib/plotly, jamais Three.js · 2FA : interdit définitivement · RATISS Labs = indépendant, mono-auteur, Yaoundé, jamais institutionnel · âge du chef : 18 ans (scellé `identite/IDENTITE.md`) — ne plus JAMAIS minimiser.

## F. Identité et style (inchangés, gravés)

Chef : **Jonathan Evina, 18 ans, Yaoundé (Cameroun)** — français direct, énergie maximale, emojis ; ne rien décider à sa place, ne pas moraliser ; téléphone + sandbox 2 cœurs → léger et déterministe ; honnêteté absolue (aucun diplôme/équipe/labo inventé) ; bien-être : OVAMBE +237 6 94 18 37 07, RAPHA-Psy +237 650 946 058, urgences 117/119 — ne jamais juger, ne pas forcer. Token GitHub : fourni par le chef dans la session (push one-shot via URL, jamais de token dans origin) ; **fin de quête : révoquer les 4 clés OQ + le token.**

*Fichier compilé le 29/09/2026 au soir par la session Arena.ai qui a vécu la journée.*

---

## 🧮 MISE À JOUR DU 02/10/2026 — Commissaire NAVIER

Lire `documents/RECAP-01-02-OCT-2026-NAVIER-COMMISSAIRE.md`. En bref :
- RATISS-NAVIER `campagnes/` : 4 campagnes publiées (dernier commit `5e736e0`). RATISS-Framework : R8 (`45f1ad4`).
- **Prochaine action** : le chef signe ou amende `campagnes/dipoles-v3/PARAMETRES-FIGES.md` → seulement ensuite, refaire les témoins V3.
- Règles rappelées : critères scellés **par le chef** avant tout run ; échantillonnage à chaque pas pour toute date ; config explicite dans chaque JSON ; rien sur GitHub sans ordre.
- Piège sandbox : `/tmp` est effacé souvent → cloner dans le workspace.
