# 🗂️ SALONS À GARNIR — MCT & IA
## 3 salons : mct-comprehension · agents-ia · ratiss-os

*Ces trois salons sont des **chantiers ouverts**. Le format dit clairement ce qui est fait et ce qui ne l'est pas.*

---

# 📌 #mct-comprehension

**« Le modèle qui ne prédit pas : qui comprend. »** 🧠

C'est la phrase du labo. Elle pose une question énorme, et ce salon est fait pour **ne pas y répondre trop vite**.

---

## ❓ La question, posée proprement

Un modèle qui prédit bien n'a pas forcément compris quoi que ce soit. Il peut très bien avoir mémorisé des corrélations.
**Alors qu'est-ce qu'on accepterait comme preuve de compréhension ?**

Et attention, la question piège derrière :
si on définit « comprendre » comme « prédire sur des cas jamais vus », on retombe sur la prédiction.
si on le définit comme « expliquer », il faut un juge, et le juge est humain donc discutable.

**Trois pistes qu'on peut tester :**
1. **Transfert** — le modèle tient-il sur un domaine qu'il n'a jamais vu, **sans réentraînement** ?
2. **Compression** — décrit-il le système avec **moins** de paramètres que nécessaire pour le mémoriser ?
3. **Contre-exemple** — sait-il dire **pourquoi** ça échoue, et pas seulement que ça échoue ?

---

## 📋 État du chantier

| | |
|---|---|
| 🚧 | concept posé, nom donné au salon |
| 🚧 | aucun résultat publié à ce jour |
| ❌ | aucune revendication de « compréhension » par le labo |

> **On ne mettra pas dans ce salon une capture d'écran de chatbot qui « comprend ».
> Ça, tout le monde sait le faire, et ça ne prouve rien.**

---

## 🎯 Ce qu'on accepte comme contribution

- un **protocole** de test de compréhension, écrit avant d'avoir le résultat
- un **contre-exemple** où un modèle prédit juste sans rien comprendre
- une **définition** de « comprendre » qui soit falsifiable

**Si tu as déjà retourné le problème dans ta tête : écris-le.** Un protocole raté reste un protocole utilisable. 🔬

---

# 📌 #agents-ia

**L'IA ici est un amplificateur, pas un oracle.** 🤖

Le labo travaille avec des agents — mais **chaque chose qu'un agent produit est vérifiée par une exécution réelle**. Sinon elle ne sort pas.

---

## 🧪 La méthode, en clair

```
1. L'agent écrit du code
2. On L'EXÉCUTE (pas « on relit »)
3. On compare la sortie à ce qui était annoncé
4. Si ça diverge → on le publie, on ne le corrige pas en douce
```

**Exemple concret du labo :** un agent produit un rapport annonçant « 20 tests passent ».
Vérification réelle → **23 tests** passent. L'écart est signalé, pas effacé. ✅

---

## ⚠️ Le piège n°1 : l'agent qui flatte

Un modèle entraîné à être agréable **te dira que ton travail est génial**. C'est exactement ce dont un chercheur n'a pas besoin.

**Trois règles à exiger d'un agent :**
- ❌ pas de chiffre qu'il n'a pas calculé
- ❌ pas de « je me souviens de toi » — il ne se souvient pas, il lit
- ✅ il doit pouvoir dire **« là, c'est faux »**, même si ça déplaît

**Un agent qui ne peut pas te contredire n'est pas un partenaire. C'est un miroir.** 🪞

---

## 🔧 Les rôles en place

| Rôle | Ce qu'il fait | Ce qu'on vérifie |
|---|---|---|
| Agent « bras droit » | audits, mesures, docs, figures | chaque chiffre est rejoué |
| Agent « codeur » | écrit les organes, pousse sur branches `atelier-*` | chaque branche est testée avant fusion |
| **Jonathan** | tranche, dirige, refuse | — |

> ⚠️ **Règle de sécurité (loi n°5) :** aucun token, aucune clé API, aucun secret **jamais** dans le chat public. Même « pour un test ». Même « je le révoque après ».

**Raconte ici ton meilleur raté avec une IA.** C'est plus instructif que les réussites. 💪

---

# 📌 #ratiss-os

**Chantier ouvert. Et ce salon commence par une question, pas par une promesse.** 💽

« RATISS OS » désigne l'idée d'un système unifié — les moteurs, le bus, les agents et les preuves dans un même ensemble cohérent.

> **État réel : rien n'est construit. Aucune ligne de ce salon ne décrit quelque chose qui existe.**
> C'est un espace pour penser à voix haute, pas une roadmap.

---

## ❓ Les questions à trancher avant d'écrire une ligne

**1. Unifié, ou seulement connecté ?**
Le bus Omni fait déjà communiquer les moteurs. Est-ce qu'« OS » veut dire *plus* que ça — ou juste un nom pour quelque chose qui existe déjà ?

**2. Qui est le noyau ?**
Aujourd'hui il n'y a que des dépôts séparés avec des imports croisés et 117 chemins absolus codés en dur. Un vrai système n'a pas de chemins codés en dur. **C'est le premier chantier, et il n'est pas glamour.**

**3. Une preuve, c'est un objet de première classe ?**
Si le sceau d'intégrité et le journal des déviations étaient **dans le système** au lieu d'être dans des fichiers annexes, est-ce que ça changerait la façon de travailler ?

**4. Et l'argent ?** 💸
Un laboratoire qui tourne a besoin d'énergie, de matériel, de temps. Aucun salon du serveur n'en parle. C'est une vraie question, pas un tabou.

---

## 📋 Ce qu'on accepte ici

- un **schéma** d'architecture, même griffonné
- une **critique** de l'existant (le plus utile, franchement)
- une **proposition de nom** moins prétentieuse, si « OS » est trop gros pour ce que c'est

**Interdit ici :** dessiner une architecture de 15 boîtes alors que zéro ligne tourne. 😄

On part de ce qui existe, et on n'ajoute qu'un étage à la fois.
