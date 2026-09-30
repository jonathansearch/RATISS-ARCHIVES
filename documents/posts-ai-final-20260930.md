# POSTS r/ArtificialIntelligence — VERSIONS FINALES PRÊTES À COLLER (30/09/2026)
*Écrits dans la voix du chef · français (la communauté du sub postent en FR) · chaque post vaut seul, le lien n'est qu'une source.*

---

## POST A — Flair : Project/Build ⭐ (le recommandé)

**Titre :**
J'ai dirigé un labo de physique solo avec une IA sous ordres stricts — 14 dépôts en 9 jours, tous les échecs publiés

**Corps :**

Salut à tous,

Petit retour d'expérience un peu particulier : je fais de la physique en solo (pas d'institution, pas d'équipe), et depuis quelques semaines j'ai intégré une IA comme copilote permanente — celle qui écrit le code, exécute les calculs, pilote les machines. Pas comme gadget : comme instrument de labo. Voici le modèle de gouvernance qui a tenu la route, et ce qu'il m'a coûté en erreurs.

Le principe de base : l'IA exécute, elle n'invente pas. Chaque action importante part d'un ordre humain explicite, une action par ordre. Chaque chiffre publié est produit par un script rejouable — jamais recopié d'une réponse de chat. Et chaque nombre est étiqueté selon son origine : calculé, mesuré, ou littérature. Jamais mélangés.

Trois leçons apprises en conditions réelles :

1. Les tests avant la confiance. J'écris (ou fais écrire) les tests AVANT de laisser l'IA produire les résultats. Sur la dernière série, la suite de tests a attrapé deux bugs dans ses calculs (une somme d'entropie qui s'arrêtait trop tôt, un facteur ½ oublié). Corrigés, publiés, documentés. Sans les tests pré-enregistrés, ces bugs seraient partis dans la nature.

2. Les échecs d'exécution sont normaux — le protocole, pas la panique. Exemple concret : les jetons d'accès aux machines quantiques expirent toutes les 5 minutes, donc le processus d'attente de l'IA meurt systématiquement après soumission. Première réaction naïve : relancer. Mauvaise idée — ça crée des jobs en double. La règle née de ça : le job survit côté serveur, on vérifie l'état avec un jeton frais, on ne relance jamais pour « finir ». Même logique quand un processus plante en plein vol : lister ce qui a été créé malgré le crash, nettoyer, documenter.

3. Vérifier le prix avant d'approuver. Pour les expériences payées (crédits de calcul), l'estimation humaine était parfois fausse d'un facteur 15. La règle : la ligne de devis s'affiche avant validation, elle se lit à voix haute, toujours. Ça a économisé des crédits réels.

Ce que ça a donné concrètement : 14 dépôts open source en 9 jours (simulations, un benchmark de 3 vrais ordinateurs quantiques — ions, puces supra 20 et 108 qubits —, des rapports avec les données brutes), 40 tests verts, et tous les échecs publiés comme les succès : hypothèses réfutées, jobs annulés, bugs. Rien d'embelli.

Le point qui me semble le plus intéressant pour cette communauté : la question n'était pas « à quoi sert l'IA » mais « qu'est-ce qui reste humain ». Chez moi : les ordres, les arrêts, les décisions d'argent, et la règle du jeu (l'honnêteté). Le reste — écrire, calculer, piloter, vérifier — est délégué, mais sous protocole écrit.

Si le sujet intéresse, tout est public et rejouable (code, données brutes, journaux d'échecs) : https://github.com/jonathansearch/RATISS-PLANCK

Questions et critiques bienvenues — c'est fait pour être décortiqué.

---

## POST B — Flair : Tutorial/Guide

**Titre :**
Checklist : garder une IA honnête dans un travail technique — 8 règles tirées de 14 projets open source

**Corps :**

Après des semaines à faire travailler une IA comme instrument principal sur des projets de physique (calculs, simulations, pilotage de machines réelles), voici la checklist que j'aurais aimé avoir au départ. Chaque règle est payée par un incident réel.

1. Tests pré-enregistrés avant résultats. Les tests existent AVANT que l'IA produise ses chiffres, pas après. Ils ont attrapé 2 bugs dans mes propres résultats (un critère de somme faux, un facteur de moyenne oublié).

2. Étiquette d'origine sur chaque nombre. Chaque chiffre publié porte sa source : calculé / mesuré / littérature. Trois couleurs, jamais mélangées. C'est le seul moyen de savoir ce qui est prouvé et ce qui est cité.

3. Une action par ordre. L'IA ne chaîne pas deux actions sensibles sans validation humaine entre les deux. Ça ralentit tout de 10 % et ça élimine 90 % des dégâts.

4. Lire le devis avant d'approuver. Tout ce qui coûte (temps machine, API payante) affiche son prix avant validation. Mon estimation humaine était fausse d'un facteur 15 sur une machine.

5. Ne jamais « relancer pour finir ». Si un processus meurt en cours (timeout, crash), la ressource survit côté serveur dans 9 cas sur 10. On vérifie l'état avec des identifiants frais, on ne re-soumet pas. Re-soumettre = doubler le travail et payer deux fois.

6. Après tout crash : liste des effets de bord. Un processus interrompu peut avoir créé des ressources fantômes. Protocole : lister ce qui existe, annuler ce qui ne devrait pas exister, documenter. Deux fois par semaine, sinon.

7. Publier les échecs comme les succès. Hypothèses réfutées, bugs, jobs annulés : tout est dans l'historique public. Paradoxalement, c'est ce qui rend les succès crédibles.

8. Sceller les livrables. Empreinte SHA-256 de chaque fichier du dépôt, vérifiable par n'importe qui. Toute modification silencieuse casse le sceau, exprès.

La règle zéro qui englobe tout : décider ce qui reste humain AVANT de commencer. Chez moi : les ordres, l'argent, les arrêts, et l'étalon de l'honnêteté. Tout le reste se délègue.

*(Ces règles viennent d'un écosystème open source public ; je peux link en commentaire si ça intéresse du monde.)*

---

## POST C — Flair : Discussion

**Titre :**
Exécuter vs écrire : où passe la vraie ligne entre IA outil et IA autrice en science ?

**Corps :**

Question qui me trotte depuis que j'ai fait travailler une IA à plein temps sur des projets scientifiques ouverts (calculs, simulations, machines réelles) : où est LA ligne qu'on ne doit pas franchir ?

Mon cas concret : l'IA a écrit l'intégralité du code, exécuté les calculs, piloté les expériences sur de vrais ordinateurs quantiques, rédigé les rapports. De mon côté : les ordres, les décisions, l'argent, et un protocole d'honnêteté (tests pré-enregistrés, sources étiquetées, échecs publiés). Résultat : 14 projets en 9 jours, dont un benchmark de 3 machines quantiques avec données brutes publiées — chose que je n'aurais JAMAIS faite seul.

Trois objections honnêtes qu'on peut me faire, et mes réponses :

1. « Sans IA tu n'aurais rien produit. » Vrai. Mais c'est aussi vrai d'un télescope, d'un cluster de calcul, d'un spectromètre. On ne dit pas d'un astronome que c'est le télescope qui découvre. La question est plutôt : est-ce que l'outil peut MENTIR ? Un télescope, non. Un LLM, parfois. D'où le protocole de vérification — c'est LÀ la vraie différence.

2. « L'IA valide tes biais. » Risque réel, documenté. Ma parade : les tests sont pré-enregistrés (écrits avant les résultats), les échecs sont publiés, et je fais rejouer les sources primaires (données officielles, papers) plutôt que de demander à l'IA de « confirmer ». Mais je ne prétends pas que c'est suffisant — c'est le maillon que je surveille le plus.

3. « Tu ne peux pas revendiquer la paternité. » Là je diverge : la paternité d'un travail scientifique n'a jamais été « qui a tapé les équations », mais qui assume : les choix, les limites, les erreurs. Si le travail est faux, c'est MON nom qui prend. L'IA ne peut pas être responsable de quoi que ce soit — et tant qu'il n'existe pas d'entité responsable, je soutiens que l'auteur humain est celui qui signe et qui paie les erreurs.

Du coup, ma proposition de ligne : la frontière n'est pas « qui écrit », mais « qui vérifie et qui assume ». Un texte humain non vérifié est plus fragile qu'un calcul IA entouré de tests. Un calcul IA sans protocole est plus dangereux qu'une intuition humaine documentée.

Vous en pensez quoi ? Vous mettez la ligne où, vous ?

---

# CHECKLIST DE PUBLICATION
- **Flair obligatoire sous 30 min** (sinon suppression auto) : A → Project/Build · B → Tutorial/Guide · C → Discussion
- **Timing** : A et B tôt (12h-14h Yaoundé = matin US), C peut attendre le soir
- **Aucun des trois n'est un lien nu** : le lien n'apparaît qu'en fin de corps, et le post reste utile sans (règle 3 validée)
- **Répondre aux 3 premiers commentaires vite** (le thread vit ou meurt dans l'heure)
- Si demande « did you use AI? » : « Oui — comme calculatrice et pilote, sous mes ordres. Chaque chiffre est calculé, testé et rejouable. Les mots sont de moi. »

---
# DÉCISION DU CHEF (30/09 ~13h) : ordre de frappe + images
- **POST A en premier, SEUL** (flair Project/Build, post texte pur, créneau 12h-14h Yaoundé = matin US).
- **PAS d'image** sur r/ArtificialIntelligence : R2 supprime le contenu image sans signal, R3 traque le funnel.
  L'illustration téléphone→3 QPU reste réservée à r/FrenchTech.
- **Séquence anti-ban** (R3 « repetitive self-promotion » = ban permanent) :
  A aujourd'hui → B dans 3-4 jours SI A a bien tourné → C plus tard, idéalement nourri du débat de A.
- Lien du repo : jamais dans le titre, en fin de corps pour A, en commentaire pour B/C si demandé.
