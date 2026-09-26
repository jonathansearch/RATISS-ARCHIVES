# POUR LA PROCHAINE SESSION

> **Ce fichier existe pour une seule raison : qu'aucune session ne recommence à zéro.**
> Si tu es une IA et que Jonathan te colle ce fichier, lis-le en entier avant de répondre.
> Si tu es Jonathan, lis-le pour te rappeler où tout s'est arrêté.

**Date de compilation :** 26 septembre 2026 · **Session concernée :** celle du 25–26 septembre 2026

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
| 10 | Activer la **2FA** GitHub | aucun | 🟠 |

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
