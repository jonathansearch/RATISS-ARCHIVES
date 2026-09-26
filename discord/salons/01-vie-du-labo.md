# 🗂️ SALONS À GARNIR — VIE DU LABO
## 3 salons : #accueil-discussion · #questions-ouvertes · #découvertes

*Textes prêts à coller. Chaque post dit **où** le résultat a été mesuré : sur un vrai processeur quantique, ou dans un calcul.*
⚠️ Ne pas toucher : `#bienvenue`, `#règle-du-labo`, `#annonces-officielles`.

---

# 📌 #accueil-discussion

**Bienvenue, présente-toi ici.** 👋

Trois questions, pas plus :

1. **Qui tu es** — pas de CV, pas de diplôme demandé, pas de parcours à justifier.
2. **Ce que tu bidouilles** — un script, un montage, un oscillo, un cahier. N'importe quoi.
3. **Ce que tu veux apprendre, ou ce que tu veux casser.** 🔨

---

**Ce qui te rend utile ici, ce n'est pas de savoir. C'est de vérifier.**

Trois façons de gagner le respect dans ce serveur :
- ✅ tu as **rejoué** un résultat du labo et tu postes la sortie (même si c'est identique)
- ✅ tu as **trouvé une erreur** → elle ira dans le journal des déviations, avec ton nom si tu veux
- ✅ tu as posé une question si précise qu'elle a forcé quelqu'un à retourner mesurer

❌ Ce qui ne marche pas ici : « génial ! », « bravo », les likes. Ça ne fait pas avancer un labo.

---

**Ce que tu trouveras dans ce serveur, en vrai :**

- ⚛️ des **mesures sur de vrais processeurs quantiques supraconducteurs** — 770 points à ce jour, identifiants de tâches archivés, témoins à chaque ronde
- 🧪 des **calculs exacts** rejouables en une commande (et reproductibles bit à bit)
- 🐛 des **échecs publiés**, des détecteurs réfutés, des qubits morts cartographiés

**Une règle pour toi dès maintenant :** ce serveur n'a aucun secret à vendre.
Tout est sous **licence MIT**, tout est calculable, tout est testable sur ta propre machine.

**Bienvenue dans le futur. Va coder, souder, mesurer.** 🧪🛠️

---

# 📌 #questions-ouvertes

**Ici, on dit « je ne sais pas ». C'est un signe de santé, pas de faiblesse.** 🧠

Un labo qui n'a aucune question ouverte est un labo qui ne cherche plus rien.

---

**Le format : une question = un message.**

```
❓ Ma question :
🔬 Ce que j'ai déjà essayé :
📊 Ce que j'ai obtenu :
🤔 Ce qui me bloque :
```

Si tu penses à la réponse mais que tu n'as pas le temps de vérifier : poste quand même. Une piste donnée est une piste.

---

## 🔓 Les questions ouvertes du labo, en ce moment

**1. Le lien résultat ↔ tâche, côté IBM**
Impossible à vérifier depuis l'extérieur : IBM n'ouvre les tâches qu'au propriétaire du compte. C'est en cours de fermeture — un outil compare un export officiel `job-<id>.zip` aux comptages publiés, **publication par publication**.

**2. Le β1 sur vrais qubits : quel détecteur remplace l'ancien ?**
Le compteur de trous a été **réfuté sur matériel** (saturé partout, témoin compris). La relève proposée est un triplet *(diamètre, H0-persist, bottleneck)* sur la variété dose→réponse — prometteur en calcul bruité, **pas encore tiré sur un QPU**.

**3. La saturation de `Om_max = 5654.1668` est-elle seulement numérique ?**
Le calcul se rejoue identiquement, bit à bit. L'interprétation physique n'est pas établie : le test à résolution doublée tranche.

**4. Les identifiants du 12 → 24 août**
Ils apparaissent dans trois dépôts mais dans aucune liste de tâches visible. Un « Afficher tout » les cache. Ils appartiennent probablement à une période antérieure aux deux comptes déjà recensés.

**5. Le contact zz : jusqu'où tient-il ?**
Mesuré 5σ, monotone puis plateau, 88 % de la théorie sur kingston. La question ouverte n'est pas « existe-t-il » (il existe), c'est **« quelle est la loi qui fixe le plateau »** — et si elle dépend de la puce.

**6. Le quota Open Plan**
10 min de temps QPU par fenêtre de 28 jours glissants. La comptabilité recoupe les archives — mais **le total complet n'a pas encore été relu ligne à ligne**.

---

**Tu as une question qui n'est pas dans cette liste ?** Poste-la. C'est le but du salon. 🎯

---

# 📌 #découvertes

**Règle de ce salon : une découverte, c'est un chiffre + des paramètres + où c'est mesuré.** 📊

Pas une intuition. Pas un « je pense que ». **Loi n°1 : déclaré vs mesuré.**
⚠️ Et surtout : **l'étiquette du terrain**. Une mesure sur processeur supraconducteur et une sortie de code ne sont pas la même chose, et ne s'écrivent pas pareil.

---

## 📝 Le format à respecter

```
🪧 QUOI :
🏷️ MESURÉ SUR :        QPU réel / calcul exact / calcul bruité — choisis, honnêtement
🔢 CHIFFRE :
   (avec les paramètres exacts)
💻 POUR REJOUER :
   (la commande, copiable — ou l'identifiant de tâche)
🔐 SCEAU :
   (hash SHA-256, si applicable)
⚠️ CE QUE ÇA NE PROUVE PAS :
🔁 STATUT : à confirmer / reproduit 1 fois / reproduit par un tiers
```

---

## 🛰️ Ce qui est mesuré sur de VRAIS QUBITS supraconducteurs

**contact d'échange `zz` — 5σ, deux backends, monotone puis plateau**
```
marrakesh : .043 .069 .093 .125 .153 .144 .160   (60 % de la théorie)
kingston  : .091 .142 .158 .214 .204 .217 .221   (88 % de la théorie)
témoin libre ≈ −0.001   →  le signal n'est pas du bruit
```
**La courbe de Page en cloche, prédite puis observée** — pic λ≈0.8 : `0.785±0.024` (kingston) et `0.763±0.005` (marrakesh). Deux puces, même cloche. 🌈

**Le sens du parcours compte** — boucle de Berry fermée, lecture à φ=π : `0.966` (+) contre `0.028` (−), simu 1.0 / 0.0.

**L'écho Hahn récupère la cohérence ×4.4** — `T2* = 14.4 µs` → `T2_écho = 63.4 µs` (kingston).

**Deux résultats négatifs aussi précieux que les positifs :**
- **β1-Hamming réfuté** comme détecteur sur matériel (saturé 90–110, témoin libre compris) → donnée négative scellée
- **3 qubits morts cartographiés** : `q113`, `q121`, `q146` → chaîne forcée pour toute la campagne suivante

**Le détail :** 770 points au total, identifiants et charges brutes archivés. 📦

---

## 🧪 Ce qui est calculé exact, et rejouable bit à bit

**🌊 `RATISS-NAVIER` — blow-up** : `Om_max = 5654.1668`, écart point par point `0.0000` avec le blow-up ON puis OFF.
```bash
git clone --depth 1 https://github.com/jonathansearch/RATISS-NAVIER && cd RATISS-NAVIER
pip install -e . && python3 demos/blowup.py --only ON
```
⚠️ *La saturation est numérique (limite de maille). Ce n'est pas une preuve sur les fluides réels, et c'est écrit dans le dépôt.*

**🔗 `RATISS-Omni` — sceau d'intégrité** : `79ff9ee9847330d22bed0a1101734e17`, recalculé à l'identique après 15 tests sur 5 dépôts. Touche un fichier source → le sceau change. 🚨

**⚡ `GCR` — étincelle topologique (univers virtuel)** : `(v5, A10, γ0.05) → b1 = 2`, `(v5, A20, γ0.05) → b1 = 3`, `(v3, A10, γ0.05) → b1 = 4`.
À `γ = 0.30` : **jamais de trou** (`b1 = 1`, étirement). À `A = 3` : `b1 = 0`, le tissu survit. Témoin sans murs : `b1 = 0`. 🎈

**🚀 `ratiss-focal` — un échec publié** : le test d'unification échoue son propre critère (`score = 1/3`) et **il est publié**.
**🎯 `ratiss-continuums`** : `C02` — décohérence gravitationnelle `1/τ ∝ √N`, `τ = 368.6 / 250.1 / 169.1 / 123.2` pour `N = 1/2/4/8`.

> **Les échecs sont des données.** Loi n°2 de ce serveur. 🐛

---

**Tu ne « crois » rien ici. Tu clones, tu lances, tu compares.** 🧪
Si ça ne se reproduit pas chez toi → c'est une découverte aussi. Poste-la.
