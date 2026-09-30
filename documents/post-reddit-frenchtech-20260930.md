# Post Reddit r/FrenchTech — 30/09/2026 (rédigé pour le chef)

**Flair recommandé : Ressource / Tuto** (alternatives : Discussion, ou Mon Projet Inutile pour l'humour auto-dérisoire)

**Titre proposé :**
J'ai fait une journée entière de physique quantique depuis un téléphone : des calculs le matin, de VRAIS ordinateurs quantiques l'après-midi — méthode et outils 100 % open source

*(Titre alternatif : « Projet perso : une journée, 3 vrais ordinateurs quantiques comparés, 40 tests verts — tout est publié en open source »)*

---

Salut les gars,

J'ai travaillé toute cette journée sur un projet perso : RATISS-PLANCK (RATISS Labs, c'est le nom de mon labo... d'une seule personne 😂). Bref, je vous raconte — parce qu'au-delà de l'anecdote, ce que je partage surtout, c'est une méthode et des outils rigoureux, gratuits et open source, pour tous ceux qui travaillent en physique (ou qui veulent s'y mettre), et plus largement pour quiconque fait de la science.

**Le concept de la journée.** Le matin, je me suis posé une question bête en apparence : « le mur de Planck, c'est quoi exactement ? ». J'ai donc tout recalculé moi-même à partir des constantes officielles (CODATA 2022), avec des scripts Python et des tests automatiques qui vérifient chaque chiffre. Verdict vulgarisé : ce n'est pas un « pixel » de l'univers — c'est le point précis où nos deux meilleures théories (mécanique quantique et relativité générale) se contredisent. Et pour sonder à cette échelle, la physique prédit qu'on fabriquerait un trou noir plus grand que la cible elle-même. Fun fact : pour concentrer l'énergie nécessaire dans une particule avec les aimants du LHC, il faudrait un anneau de 516 années-lumière. Pas demain la veille.

**L'après-midi, le tournant.** Plutôt que de rester sur le papier, je suis allé sur une plateforme cloud (Open Quantum) qui loue l'accès à de VRAIS ordinateurs quantiques — des ions piégés, des puces supraconductrices. J'ai lancé des expériences réelles, une par une, en lisant le prix de chaque tir avant de valider (ça se compte en crédits, comme n'importe quel cloud) :

- une paire intriquée de type Bell : 99,6 % de réussite — la machine la plus chère est aussi la plus pure ;
- des états intriqués de 3, 4, 5 puis 7 particules, sur trois machines différentes (12, 20 et 108 qubits) ;
- et le clou : un « chat » de 12 qubits intriqués en même temps, à 66 % de fidélité — le plus grand état jamais produit par le projet.

Au passage, j'ai documenté une petite loi pratique inattendue : quand on essaie de faire plusieurs expériences dans un seul tir pour économiser, ça ne marche que sur certains types de machines — le logiciel de compilation déborde des frontières des compartiments et tout se mélange. Mêmes circuits, même machine, même heure : 45 % contre 94 %. Des chiffres propres pour isoler exactement d'où vient le problème.

**Ce que je partage vraiment (c'est là que vous pouvez en profiter).** Le dépôt n'est pas un simple showcase :

- une MÉTHODE : chaque chiffre est calculé par un script rejouable, jamais recopié ; 40 tests automatiques verts ; les échecs et les bugs sont publiés comme les succès ; chaque nombre est étiqueté selon son origine (calcul / vraie machine / littérature), jamais mélangés.
- des OUTILS : les scripts de calcul physique, ceux qui pilotent les vraies machines (soumission de jobs, lecture des devis, récupération des données brutes), et un « sceau » SHA-256 qui détecte la moindre modification du dépôt.
- le tout en licence MIT, rejouable en une commande, sans dépendance exotique.

Et pour être 100 % clair sur l'honnêteté : je ne prétends avoir découvert quoi que ce soit sur la structure de l'univers. J'ai vérifié des outils, comparé trois architectures quantiques et tout documenté — y compris ce qui n'a pas marché (une hypothèse réfutée, des jobs annulés, des crédits économisés au passage). C'est justement ça, la méthode.

**Appel à la contribution.** C'est un projet indépendant (depuis Yaoundé, avec un téléphone 😄) et il est fait pour grandir avec d'autres :

- étudiant / curieux : clônez le dépôt, rejouez la journée entière, modifiez les circuits, lancez vos propres expériences ;
- chercheur / ingénieur : testez la loi « épisodique » sur d'autres backends, critiquez la méthode, ouvrez des issues ;
- développeur : tests, CI, portage vers d'autres SDK — le dépôt est volontairement petit et lisible.

Le lien ultra explicite (README complet, rapport final, chronique de la journée, données brutes, tout est là) :

👉 **https://github.com/jonathansearch/RATISS-PLANCK**

Questions et critiques bienvenues — c'est fait pour ça. 🙏

---
*Note interne : pas d'âge mentionné dans le post (demande du chef — les curieux le verront dans le dépôt). Rien d'inventé : tous les chiffres du post sont réels et calculés.*

---

# VERSION COURTE (30/09 matin — choix du chef : « trop long, personne ne lit »)

**Titre :** J'ai piloté de vrais ordinateurs quantiques depuis mon téléphone (projet open source)

Salut les gars,

Journée perso un peu folle : le matin je recalcule le « mur de Planck » en Python (des scripts + tests automatiques, chaque chiffre vérifié), l'après-midi je loue de vrais ordinateurs quantiques sur une plateforme cloud et je fais tourner de vraies expériences.

Le résultat en 3 chiffres :

- une paire de photons intriqués réussie à **99,6 %**
- un état de **12 qubits intriqués en même temps** à 66 % (le plus gros du projet)
- 3 machines différentes comparées (12, 20 et 108 qubits) — et la surprise : la plus grosse est la moins chère 😂

Tout est publié : le code, les données brutes, les échecs compris (licence MIT, une commande pour tout rejouer). L'idée, c'est de partager une méthode de travail rigoureuse et gratuite pour tous ceux qui font de la physique ou veulent s'y mettre.

Critiques, questions, contributions : bienvenues. 🙏

👉 https://github.com/jonathansearch/RATISS-PLANCK
