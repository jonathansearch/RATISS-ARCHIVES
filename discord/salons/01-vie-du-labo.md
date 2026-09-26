# 🗂️ SALONS À GARNIR — VIE DU LABO
## 3 salons : #accueil-discussion · #questions-ouvertes · #découvertes

*Textes prêts à coller. Style aligné sur tes 3 lois. Chaque post contient du **mesuré**, pas du déclaré.*
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

**1. Les 12 identifiants du 12–24 août**
Ils apparaissent dans les dépôts (`RATISS-ODV-AEON`, `Algorithmes-quantique`, `decoherence-engine`) mais dans aucune liste de tâches visible. Un « Afficher tout » les cache. Sur quel compte ?

**2. `synchrotron-24`, Λ = 0.002 : lié ou déchiré ?**
Le JSON publié dit `RIP`, ma reproduction dit `LIE`. C'est **exactement** le point sur la séparatrice (entre 0.002 et 0.005). Sensible au code, pas à la physique — mais pas tranché.

**3. Le blow-up Navier-Stokes : saturation numérique ou singularité réelle ?**
Le calcul se rejoue identiquement (`Om_max = 5654.1668`). L'**interprétation** physique, elle, n'est pas établie.

**4. Le lien résultat ↔ tâche, côté IBM**
Impossible à vérifier depuis l'extérieur : IBM n'ouvre les tâches qu'au propriétaire du compte. C'est en cours de fermeture.

**5. Le quota Open Plan tient-il ?**
85 tâches sur ~45 jours, ~2-3 s chacune, sur un quota de 10 min / 28 jours. La comptabilité recoupe — mais personne n'a encore relu le total complet.

---

**Tu as une question qui n'est pas dans cette liste ?** Poste-la. C'est le but du salon. 🎯

---

# 📌 #découvertes

**Règle de ce salon : une découverte, c'est un chiffre + des paramètres + un hash.** 📊

Pas une intuition. Pas un « je pense que ». **Loi n°1 du labo : déclaré vs mesuré.**

---

## 📝 Le format à respecter

```
🪧 QUOI :
🔢 CHIFFRE MESURÉ :
   (avec les paramètres exacts)
💻 POUR REJOUER :
   (la commande, copiable)
🔐 SCEAU :
   (hash SHA-256, si applicable)
⚠️ CE QUE ÇA NE PROUVE PAS :
🔁 STATUT : à confirmer / reproduit 1 fois / reproduit par un tiers
```

---

## 🧪 Ce qui est déjà dans ce salon (publié)

**🌊 `RATISS-NAVIER` — blow-up**
`Om_max = 5654.1668` · reproduit **bit à bit** (écart point par point `0.0000` sur 11 points)
```bash
git clone --depth 1 https://github.com/jonathansearch/RATISS-NAVIER && cd RATISS-NAVIER
pip install -e . && python3 demos/blowup.py --only ON
```
⚠️ *Le calcul se reproduit. L'interprétation « singularité réelle » n'est pas établie.*

**🔗 `RATISS-Omni` — sceau d'intégrité**
`79ff9ee9847330d22bed0a1101734e17` · recalculé à l'identique après 15 tests sur 5 dépôts
```bash
python3 redteam/bench.py
```

**🎯 `GCR` — étincelle topologique**
`b1_max = 2` pour A=10, γ=0.05 · et `b1_max = 1` (pas de déchirure) pour γ=0.3
```bash
python3 -m pytest tests/ -q     # 4 passed
```

**🧬 `synchrotron-24` — seuil de séparatrice**
entre Λ = 0.002 (dernier **lié**) et 0.005 (premier **RIP**)
⚠️ *12 des 13 valeurs de Λ reproduites au chiffre près. La 13ᵉ diverge → journal des déviations.*

**📉 `ratiss-focal` — un échec publié**
`exp63` → `score = 1/3`, publié tel quel. `exp61` → `IRRÉVERSIBLE`.
**Les échecs sont des données.** Loi n°0 de ce serveur.

---

**Tu ne « crois » rien ici. Tu clones, tu lances, tu compares.** 🧪
Si ça ne se reproduit pas chez toi → c'est une découverte aussi. Poste-la.
