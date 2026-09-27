# POUR LA PROCHAINE SESSION

> **Ce fichier existe pour une seule raison : qu'aucune session ne recommence à zéro.**
> Si tu es une IA et que Jonathan te colle ce fichier, lis-le en entier avant de répondre.
> Si tu es Jonathan, lis-le pour te rappeler où tout s'est arrêté.

**Date de compilation :** 26 septembre 2026 · **Session concernée :** celle du 25–26 septembre 2026
**MISE À JOUR 27/09 :** PHOTON + ETALONS publiés, hub Discord 22 salons, audit finance → lire la
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
Les 24 posts de salons Discord sont dans `discord/salons/` (index de copie : `discord/salons/INDEX.md`).

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
