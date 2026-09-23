# VigilanceCanicule
Avec un été caniculaire en France, je souhaite connaitre le nombre de jours en alerte canicule durant l'année 2026, et l'évoluation de ce nombre sur les dernières années. Ce projet est dédié à l'exploitation des données Météo France existantes à cette adresse : 
https://files.data.gouv.fr/meteofrance/data/vigilance/metropole/

Il n'y a des données que depuis novembre 2022.

### Approche initiale : ###
Le code repose sur l'extraction des vigilances canicules dans les fichiers CDP_TEXTE_VIGILANCE.json. Ceux-ci n'existent malheureusement pas pour tous les jours, même si c'est le cas pour la majorité des jours entre mai et octobre. 
Le décompte ainsi obtenu des jours en alerte canicule est un minimum.

### Approche retenue : ###
Les fichiers CDP_CARTE_EXTERNE.json étant présent pour chaque jour de l'année (relatif à la carte de vigilance), c'est sur ceux-ci que se baseront l'extraction des jours de canicule. Par comparaison entre les cartes et les fichiers json associés, on supposera :
  phenomenon_id	== "6" correcpond à une vigilance canicule
  phenomenon_max_color_id correspond au niveau d'alerte (1 = vert, 2 = jaune, 3 = orange, 4 = rouge)

### Dans les deux approches : ###
Le décompte imparfait car prise en compte uniquement des bulletins vigilance de 6h chaque jour (les vigilances pouvant se mettre en place plus tardivement dans la journée).


