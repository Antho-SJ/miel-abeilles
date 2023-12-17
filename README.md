  Le code joint génére une ruche de 100 abeilles qui seront caractérisées par leur distance parcourue dans un champ.
Ce champ est composé de 50 fleurs et chacune des abeilles parcourent ces 50 fleurs une fois par jour.
Pour générer une nouvelle génération, on gardera les 50 meilleures abeilles, qui se reproduiront ensemble.

  Il y a quelques degrès de liberté dans ce projet, comme la manière dont on selectionne les parents pour la reproduction,
ainsi que la façon de les reproduire et la méthode utilisée pour générer des mutations dans l'ADN.

  De plus j'ai choisis de randomiser un maximum, effectivement mon aléatoire n'est pas une seed mais un aléatoire complet.
Il est donc compliqué de comparer efficacement deux résultats différents.

  Pour la reproduction, j'ai choisi de toujours reproduire la meilleur abeille avec la "pire" parmi les 50 et ansi de suite.
La reproduction est modélisée par une fonction avec un point de croisement, qui est à chaque fois aléatoire.

  Pour finir, j'ai choisi pour les mutations d'échanger deux tuples aléatoires dans la séquence des abeilles touchées.
Cette mutation touche 9 à 15% des abeilles lorsqu'elle survient.

  Piste d'amélioration : changer de fonction de reproduction, ainsi que de mutation.
Les mutations sont déclanchées que lorsque l'algo retourne la même moyenne de score deux générations d'affilées,
il serait préférable d'établir plutôt un seuil, par exemple (si |moyenne1 - moyenne2| < epsilon : déclancher mutation).
