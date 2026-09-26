# 🗂️ SALONS À GARNIR — ATELIER
## 4 salons : cours-c-electronique · travail-chez-le-maitre · resultats-mesures · carnet-de-pannes

*L'ATELIER, c'est l'ancrage matériel. Après le cloud et les simulations, la matière sous les doigts.*

---

# 📌 #cours-c-electronique

**Apprendre le C et l'électronique, pour de vrai, avec un fer à souder et un oscilloscope.** 🔧

C'est le salon du **côté matériel** du labo. Ici on ne parle pas de frameworks et d'abstractions : on parle de composants, de schémas, de tensions et de code qui doit tenir dans un microcontrôleur.

---

## 📚 Le plan, en trois couches

**1. Le langage C** — pas pour « faire du dev », mais pour **parler au matériel** :
pointeurs et adresses, registres, interruptions, gestion de la mémoire à la main.
*Pourquoi : une commande Python, personne ne peut la vérifier physiquement. Un firmware, oui.*

**2. L'électronique de base** — lire un schéma, choisir une résistance, comprendre un condensateur, respecter une polarité, éviter de griller la carte. ⚡

**3. L'instrumentation** — oscilloscope, multimètre, alimentation de labo.
**Une mesure sans instrument, c'est une opinion.** Même loi qu'en simulation : déclaré vs mesuré.

---

## 🔬 Ce qui se passe ici concrètement

**Le format des posts :**
```
🧠 CE QUE J'APPRENDS :
🔌 CE QUE J'AI MONTÉ :
📉 CE QUI A GRÉSILLÉ :
❓ MA QUESTION :
```

**Les questions « bêtes » sont bienvenues.** Si tu ne comprends pas pourquoi une LED a besoin d'une résistance, pose la question — c'est une vraie question, et beaucoup de gens n'osent pas la poser. 🛡️

**Aucune question n'est trop simple ici.** Le seul truc qui n'est pas toléré : faire semblant d'avoir compris. 🤝

---

# 📌 #travail-chez-le-maitre

**23 ans d'expérience. Formation allemande. Avenue Kennedy, Yaoundé.** 🇩🇪🇨🇲

Ce salon est le **journal d'apprentissage** d'un autodidacte chez un artisan qui sait faire.

> Pourquoi c'est important : un mois de cloud et de simulations, ça fait vivre la tête. Le fer à souder fait vivre les mains.
> Les deux ensemble, ça fait un chercheur. **Un seul des deux, ça fait quelqu'un qui se raconte des histoires.**

---

## 🛠️ Ce qu'on apprend dans un vrai atelier

- **La rigueur du geste** — un fil mal dénudé, un composant monté à l'envers, et ça ne marche pas. Le matériel ne négocie pas. 💪
- **Le diagnostic** — trouver la panne sans la voir, par déduction et par mesure
- **L'économie de moyens** — faire avec ce qu'on a, pas avec ce qu'on commanderait
- **L'humilité** — celui qui a 23 ans de métier connaît des choses qui ne sont écrites dans aucun manuel

---

## 📝 Le format du journal

```
📅 JOUR X
🔧 CE QU'ON A FAIT :
🤯 CE QUE J'AI COMPRIS (ou pas) :
⚡ LA PHRASE DU MAÎTRE :
📸 PHOTO / SCHÉMA :
```

**C'est aussi un carnet de mémoire.** Dans six mois, ces notes vaudront plus qu'un long rapport : elles montreront d'où tu viens.

---

## 🎯 Ce que ce salon montre au monde

Que la science ne commence pas dans un cloud. Elle commence **dans des mains**.
C'est le salon le moins « tech » du serveur, et probablement le plus important. ❤️

---

# 📌 #resultats-mesures

**Une mesure sans incertitude n'est pas une mesure. C'est une affirmation.** 📊

Ce salon est la **traçabilité matérielle** du labo : tout ce qui sort d'un instrument physique — oscilloscope, multimètre, VNA — et pas d'un simulateur.

---

## 📝 Le format obligatoire

```
📅 DATE :
🔬 INSTRUMENT :          (marque/modèle, ou « inconnu » si tu ne sais pas)
📐 MESURE :              valeur ± incertitude
🌡️ CONDITIONS :          température, tension, fréquence, ce qui peut la faire bouger
📈 TRACE :               photo, CSV, capture d'écran
🔁 RÉPÉTABILITÉ :        1 fois / 3 fois / 10 fois
⚠️ CE QUI POURRAIT FAUSSER LA MESURE :
```

**La dernière ligne est la plus importante.** C'est celle qui distingue un laboratoire d'une démonstration.

---

## 🧪 Peu de choses ici pour l'instant — et c'est dit

Le labo a produit beaucoup de **simulations** et de **tâches sur QPU distant**. Les mesures faites **à la main**, dans un atelier, avec un instrument qu'on tient, sont encore rares.

**Ce salon va donc se remplir lentement.** C'est normal : une mesure au banc prend mille fois plus de temps à produire qu'un run de simulation. ⏳

---

## 🔗 L'articulation avec les autres salons

| Salon | Type de preuve |
|---|---|
| `#découvertes` | sortie de code, avec hash |
| `#qpu-live` | tâche distante, avec identifiant archivé |
| **`#resultats-mesures`** | **instrument physique, avec incertitude** |

Les trois ne valent pas la même chose, et le labo ne les mélange jamais.

> **Règle :** une simulation **n'est pas** une exécution matérielle.
> Un identifiant de tâche **n'est pas** une revalidation en temps réel.

---

# 📌 #carnet-de-pannes

**Loi n°2 du labo : les bugs se documentent, ils ne se cachent pas.** 🐛

Ce salon est le plus utile du serveur, et celui que tout le monde veut cacher.
**Ici, on expose les pannes.**

---

## 🏆 La panne fondatrice : `dt = 4 ns`

Un décalage de pas de temps qui a faussé une série de résultats. Des heures perdues à chercher la physique, alors que le problème était dans **une ligne de configuration**.

**Ce qui a été appris :** *toujours vérifier l'unité avant de vérifier la théorie.* ⏱️
Leçon intégrée depuis : les paramètres sont désormais **scellés et hashés avant la mesure**.

---

## 📋 Le format obligatoire

```
💥 SYMPTÔME :           ce que je voyais (le message, le chiffre bizarre)
🔍 ¿IM ? DIAGNOSTIC :   comment je l'ai trouvé
💡 CAUSE RÉELLE :       la vraie cause (souvent différente de l'intuition)
🔧 CORRECTIF :          ce que j'ai changé
⏱️ TEMPS PERDU :
📌 LEÇON RETENUE :      une phrase, réutilisable
```

La ligne **« temps perdu »** n'est pas là pour faire joli : c'est un **coût**, et un coût documenté devient une décision d'ingénierie.

---

## 🎯 Pourquoi c'est public

Parce qu'une panne cachée **reviendra**. Et parce qu'un débutant qui lit ce salon perdra trois heures au lieu de trois semaines. 🤝

**Cherche ici avant de poster une question** : la réponse y est peut-être déjà, écrite par quelqu'un d'aussi perdu que toi à ce moment-là.

---

## 🧾 Quelques pannes déjà connues à documenter

- le `dt = 4 ns` (fondateur) 📌
- les **117 chemins absolus** `/home/user/...` codés en dur dans les dépôts → tout casse dès qu'on clone ailleurs
- `ratiss-continuums/c01` : sampler **sans graine fixée** → résultats non reproductibles au bit près
- `synchrotron-24/s04` : divergence sur **λ = 0.002**, pile sur la séparatrice
- `RATISS-Omni` : deux révisions Git vides dans le sceau du bench

**Chacune de ces lignes est un ticket ouvert.** Prends-en une, corrige-la, documente-la, poste. 🛠️
