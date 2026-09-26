# 🔌 CI + DISCORD — installation en 10 minutes

But : que le labo **pousse lui-même** ses résultats dans Discord (tests, empreintes, campagnes)
sans que tu copies-colles quoi que ce soit à la main.

**Ce qui va tourner :** à chaque `git push`, GitHub exécute une vérification et poste le résultat dans un salon.
Coût : **0 €**. Hébergement : **aucun** (c'est GitHub qui travaille).

---

## 1️⃣ Créer le webhook (2 min) 🪝

Dans Discord, **sur le salon qui doit recevoir les messages** :

1. clic droit sur le salon → **Modifier le salon**
2. onglet **Intégrations** → **Webhooks** → **Nouveau webhook**
3. Nom : `RATISS CI` · Salon : celui que tu veux
4. **Copier l'URL du webhook** → elle ressemble à
   `https://discord.com/api/webhooks/1234…/AbCd…`

**Quel salon ?** Reco : crée **`#ci-alertes`** (catégorie ACCUEIL, à côté de `#annonces-officielles`).
Sinon `#resultats-mesures` fait très bien l'affaire.
⚠️ On ne touche pas à `#bienvenue`, `#règle-du-labo`, `#annonces-officielles`.

---

## 2️⃣ Où coller l'URL (1 min) 🔐

**Dans GitHub**, jamais dans Discord :

> dépôt → **Settings** → **Secrets and variables** → **Actions** → **New repository secret**
> **Name :** `DISCORD_WEBHOOK`
> **Secret :** *colle l'URL* → **Add secret**

**Loi n°5 du labo :** aucun token, aucune clé dans le chat public. Un webhook est une clé :
qui l'a peut écrire dans ton salon. Il vit dans **les secrets GitHub**, point.

---

## 3️⃣ Activer le workflow (1 min) ⚙️

Le fichier `.github/workflows/notifier-discord.yml` est déjà dans le dépôt.

1. Pousser le dépôt (`git push`)
2. Onglet **Actions** → si GitHub demande, cliquer **« I understand my workflows, go ahead and enable them »**
3. **Notifications Discord** → bouton **Run workflow** → **Run workflow**

→ Un message arrive dans le salon : ✅ `50/50 empreintes conformes`.

Ensuite, **ça se déclenche tout seul** : à chaque `push` sur `main`, et chaque **lundi 08:00 UTC** (vérification automatique).

> 🔑 **Si le `git push` est refusé** : ton token GitHub doit avoir la case **`workflow`** cochée, sinon GitHub n'accepte pas d'envoyer un fichier dans `.github/workflows/`.

---

## 4️⃣ Tester depuis ta machine (optionnel) 💻

```bash
cd RATISS-ARCHIVES
python3 outils/notifier_discord.py --test
```

Si le webhook n'est pas dans l'environnement :

```bash
echo "https://discord.com/api/webhooks/…" > ~/.ratiss-webhook
chmod 600 ~/.ratiss-webhook          # lisible par toi seul
python3 outils/notifier_discord.py --test
```

Vérifier le message **sans rien envoyer** : `--dry-run`.

Autres usages utiles depuis la ligne de commande :

```bash
python3 outils/verifier_manifeste.py                          # 50 conformes, 0 problème
python3 outils/notifier_discord.py --statut OK    --titre "Campagne QPU terminée" --details "436 points · 7 tâches"
python3 outils/notifier_discord.py --statut ECHEC --titre "synchrotron s04" --details "λ=0.002 : LIE ≠ RIP"
```

Le message est un **embed** avec ✅ / ❌ / 🔵, et il **ne peut pas** mentionner `@everyone` : c'est verrouillé dans le script.

---

## 5️⃣ Brancher les autres dépôts 🧩

Pour chaque dépôt de code (`GCR`, `RATISS-QVM`, `RATISS-NAVIER`…) :

1. copier `discord/CI-modele-tests-depots.yml` → `RATISS-XXX/.github/workflows/tests-discord.yml`
2. ajouter le **même** secret `DISCORD_WEBHOOK` dans ce dépôt
3. remplir `COMPAGNONS` si le dépôt a des imports croisés :

| Dépôt | `COMPAGNONS` |
|---|---|
| `GCR` | *(vide, autonome)* |
| `RATISS-QVM` | *(vide)* |
| `RATISS-NAVIER` | *(vide)* |
| `RATISS-NUCLEAIRE` | `"RATISS-NAVIER RATISS-FUSION"` |
| `RATISS-Omni` | `"RATISS-NAVIER RATISS-QVM"` |

**Le détail qui débloque tout :** les dépôts utilisent des chemins absolus `/home/user/<dépôt>`.
Le modèle **recrée `/home/user` dans le runner GitHub** et clone dedans → les tests tournent **tels quels**, sans modifier une ligne de code. 🎯

**Ordre conseillé :** `RATISS-ARCHIVES` (fait) → `GCR` → `RATISS-QVM` → le reste.

---

## 🤖 Et le bot Discord ? Pas maintenant.

| | Webhook | Bot |
|---|---|---|
| Effort | 10 min | créer l'app, token, permissions, héberger 24/7 |
| Hébergement | **aucun** | un serveur qui tourne en permanence |
| Ce qu'il sait faire | **pousser** des messages | lire, réagir, commandes slash `/status` `/tests` `/repos` |
| Risque | une URL à garder secrète | un **token** à garder secret + permissions à cadrer |

**Reco : webhook d'abord** — il couvre 90 % du besoin pour 0 € et 0 maintenance.
Le bot viendra quand tu voudras **interroger** le labo depuis Discord (`/status`). Ce jour-là, il faudra un hébergeur qui tourne en continu — ce n'est pas le même chantier. 🔧

---

## 🧾 Récapitulatif — 5 lignes

1. Webhook créé sur le salon → URL copiée
2. URL dans **GitHub → Secrets → `DISCORD_WEBHOOK`**
3. **Actions → Notifications Discord → Run workflow** → premier message
4. (`git push` exige le scope **`workflow`** sur le token)
5. Ensuite : automatique à chaque push + chaque lundi

---

## 🏷️ Annexe — profil du serveur (description + tags)

À coller dans **Profil du serveur** (l'écran où il y a « Attention, il reste des modifications non enregistrées ! ») :

**Description** (185 caractères, la limite Discord est de 300) :
```
Laboratoire ouvert né à Yaoundé. Mesures sur vrais processeurs quantiques, calculs rejouables, échecs publiés comme les victoires. Aucun diplôme requis : des chiffres et des témoins. MIT.
```

**Tags** — 5 max, **20 caractères max chacun**. Ta 4ᵉ étiquette est coupée (« open source et M ») parce qu'elle dépasse :
```
Science · transdisciplinaire · découvertes · open source · ouvert à tous
```
→ remplace « open source et M… » par **`open source`** tout court, sinon l'affichage casse. ✅
