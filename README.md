# La-Rape-IA

La Rape est un gadget de jeu conçu pour résoudre le problème récurrent de manquer d'idées dans divers jeux, notamment Action ou Vérité. Il utilise une chaîne de Markov pour générer des propositions aléatoires, offrant une solution au défi de devoir continuellement trouver des idées astucieuses soi-même. Les propositions disponibles en ligne sont souvent limitées et répétitives, rendant difficile le maintien de l'intérêt du jeu à long terme. Avec La Rape, les joueurs peuvent profiter d'une variété infinie de suggestions nouvelles et divertissantes, améliorant ainsi l'expérience globale du jeu.

Nous présentons une méthode innovante pour générer des idées en utilisant Markovify, un générateur d'apprentissage automatique simple basé sur les chaînes de Markov. Markovify prédit le mot suivant en fonction du mot précédent, plutôt que de toute la phrase. Cette limitation, où le modèle ne comprend pas vraiment le sens de chaque phrase, conduit à l'absurdité des propositions et renforce leur imprévisibilité. En incorporant une gamme diversifiée d'entrées, allant de l'absurde au sérieux, Markovify peut créer une multitude de défis pour les joueurs, allant au-delà de l'imagination humaine.

### Pourquoi utiliser une chaîne de Markov ?

Une chaîne de Markov est un modèle stochastique qui génère des résultats aléatoires basés sur des probabilités. En génération de texte, un modèle de chaîne de Markov prédit le mot suivant en fonction du mot précédent. Contrairement aux modèles de génération de texte pré-entraînés comme GPT-3, les modèles de chaîne de Markov ont une compréhension très limitée du texte d'entrée, ce qui donne des résultats souvent incohérents. Cette absurdité inhérente rend les applications primitives de l'apprentissage automatique parfaitement adaptées à la nature ludique du jeu Action ou Vérité, démontrant que les "erreurs" de l'apprentissage automatique peuvent être divertissantes lorsqu'elles sont bien utilisées.

De plus, les modèles d'IA pré-entraînés sont complexes et gourmands en ressources, nécessitant une puissance de calcul importante et du matériel avancé. Ils mettent également plus de temps à s'entraîner et à s'exécuter, ce qui est peu pratique pour un outil de jeu. Malgré leur sophistication, ces modèles produisent toujours des résultats imprévisibles.

Markovify, étant un modèle plus simple et plus léger, est plus écologique et convivial. Pour la tâche simple de générer des propositions pour Action ou Vérité, Markovify est un choix supérieur en raison de son efficacité et de sa facilité d'utilisation.

### Entrée sélectionnée et tests

Nous avons utilisé Markovify, un générateur de chaîne de Markov simple et extensible, pour produire des phrases basées sur des entrées utilisateur. Par exemple, si l'entrée est "Alice au pays des merveilles", la sortie pourrait ressembler à quelque chose comme « Alice pensa qu'elle ferait aussi bien de regarder et de voir ce qui n'allait pas avec ça », ce qui semble être une citation du livre mais est en réalité généré. Pour créer des défis, nous avons saisi des phrases ou instructions. Initialement, nous avons testé avec 260 propositions d'Action collectées sur des sites web. Les résultats étaient prometteurs, mais la taille limitée des entrées a conduit le modèle à simplement réorganiser les phrases selon les règles de la langue.

Puisque les défis disponibles en ligne sont limités, nous avons élargi nos entrées à d'autres sources instructives pour créer des résultats plus variés et absurdes. Cette approche a non seulement augmenté l'absurdité des propositions mais a également amélioré la créativité de la machine.

Nous avons catégorisé les entrées pour des scénarios spécifiques. Par exemple, une recette de cocktail générée aléatoirement à partir d'une liste de recettes peut être utilisée dans un bar, incitant les joueurs à commander des "boissons aventureuses" basées sur la recette générée. De même, une instruction d'exercice insensée peut servir de défi humoristique dans le jeu.

Après des tests approfondis avec diverses combinaisons d'entrées, nous avons sélectionné huit sources d'entrées divisées en cinq catégories :

  1- Action ou Vérité : Généré à partir de propositions d'Action et Vérité collectées sur internet.
  2- Citations de rap : Sélectionnées sur internet avec ChatGPT.
  3- Citations célèbres : Sélectionnées sur internet avec ChatGPT.
  4- Textes aléatoires : Sélectionnés sur internet avec ChatGPT.
  5- Noms et descriptions de dinosaures : Sélectionnés sur internet avec ChatGPT.

En utilisant Markovify avec ces entrées diverses et catégorisées, nous avons conçu une gamme de propositions créatives et divertissantes pour divers scénarios de jeu.

### “Ajustements”

En raison de la nature imprévisible de l'apprentissage automatique et du principe de génération "immature" de notre modèle, les propositions générées ne font souvent pas complètement sens pour les humains. Le taux de réussite pour produire des phrases compréhensibles est inférieur à 50 % sans modifications supplémentaires. Nous avons donc mis en œuvre une série de procédures d'« ajustement » pour améliorer la qualité des sorties en ajoutant des contraintes afin de minimiser les phrases incohérentes ou erronées.

Nous avons modifié le script Python pour nettoyer le texte d'entrée, en supprimant les symboles et espaces inutiles spécifiques à chaque type d'entrée. Par exemple, les propositions d'Action sont souvent accompagnées de puces numérotées, et les recettes de cocktails contiennent de nombreux codes “\n” et “\r” dans le texte.

Malgré ces ajustements, nous ne pouvons garantir que 100 % des propositions générées seront compréhensibles, même après ajustement. De plus, avec une entrée suffisamment large, les résultats peuvent varier considérablement, et il est difficile de prédire si la même proposition sera générée à nouveau. Il devrait donc y avoir une marge d'erreur de 10 à 26 %, selon les catégories d'entrée.

### Résultats générés - Exemples

De notre analyse, il est évident que les défis Action ou Vérité, les noms de dinosaures, et les citations de rap produisent des résultats particulièrement réussis. Markovify transforme efficacement des entrées sérieuses en propositions absurdes dans ces catégories.

Pour les défis traditionnels générés à partir des propositions collectées en ligne, la machine tente de réorganiser les entrées limitées pour générer de nouvelles phrases, avec des degrés de succès variables.

Nous avons rassemblé quelques résultats intrigants issus des cinq catégories, illustrant la diversité et la créativité des propositions générées.

#### Différents jeux :

  - Action ou Vérité
  - Citations de rap
  - Citations célèbres
  - Textes aléatoires
  - Nom de dinosaures
  - Description de dinosaures

# Commencer

Aujourd'hui on va voir comment utiliser la Rape de l'atelier IA quoi là dedans ? On va déjà vérifier si vous avez tous le matériels à disposition. 
Pour commencer, ils vous faut un ordi et de préférence l'ordinateur a titré à la rape IA. Pour que tous fonctionne correctement et au cas ou vous n'avez pas le bon ordinateur on va tous réinstaller pour etre sur.
Donc sur le bureau de l'ordinateur vous devait avoir un premier fichier qui s'apelle "TROUBLEMAKER-screen" dans ce fichier vous aurez normalement 2 dossiers, ".vscode" et "TM-SCREEN".
Vous devez aussi avoir tous ces fichiers là :
  - actions_verites.txt
  - aleatoire.txt
  - citations_celebres.txt
  - combo.txt
  - dinosaures_descriptions.txt
  - dinosaures_noms.txt
  - donnees_participants.txt
  - generer_phrase_basique.py
  - generer_phrase_bouton.py
  - Lexique code TM.txt
  - paramétrage_arduino.ino
  - rap.txt
  - readme.md
