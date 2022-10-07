# Note de cours du vendredi 7 octobre
## convertir un nombre réel décimal en binaire méthode 1
Un nombre décimal revient à 2 nombre entier avec une virgule entre les 2 qui fait que l'entier à gauche de la virgule devient décimal. 
par exemple :<br />
pour (12,6875)<sub>10</sub>
(12)<sub>10</sub> = (1100)<sub>2</sub>
pour les chiffre après la virgules on fait :<br />
0,6875 * 2 = 1,3750<br />
on prend le 1 et on le rajoute après la virgule : (1100,1)<sub>2</sub><br />
0,375 * 2 = 0,750<br />
on prend le 0 et on le rajoute après la virgule : (1100,10)<sub>2</sub><br />
0,750 * 2 = 1,5<br />
on prend le 1 et on le rajoute après la virgule : (1100,101)<sub>2</sub><br />
0,5 * 2 = 1<br />
on prend le 1 et on le rajoute après la virgule : (1100,1011)<sub>2</sub><br />
## exercice 19
### convertir les chiffres à virgules en binaire avec la méthode expliqué plus haut : 3,5 ; 4,14 ; 11,3
(3,5)<sub>10</sub> = (11,1)<sub>2</sub><br />
(4,14)<sub>10</sub> = (100,0010001111110111000011...)<sub>2</sub><br />
(11,3)<sub>10</sub> = (1011,01001...)<br />
### récapitulatif exercice
cette méthode donne en binaire des nombre infini alors qu'ils sont finis en décimal
## convertir un nombre réel décimal en binaire méthode 2
[![Voir la vidéo sur les nombres flottants](https://img.shields.io/badge/Vid%C3%A9o%20%C3%A0%20regarder-Les%20nombres%20flottants-blue)](https://youtu.be/mtizhxkB-Zw)