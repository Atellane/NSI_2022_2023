# note de cours du vendredi 21 octobre
## exercice 25 [(chapitre 2 teams)](https://teams.microsoft.com/_#/school/ClassNotebook/G%C3%A9n%C3%A9ral?threadId=19:HSHKfbWjr9-G7aq6YrMXDaGG3IgxQCmAilRAEEfGofw1@thread.tacv2&ctx=channel&isTeamLevelApp=true) :
algorithme indice du premier entier pair :
```
// *_données :_* la suite de chiffre T
// *_Résutat :_* indice du premier entier pair de T
i = 0 // indice courant
_répéter :_
    i = i+1
    _tant que_ T[i] modulo 2 == 1 et i <= longueur T
// *_sortie :_* si = T+1 _alors_ afficher 0 _sinon_ afficher i

// ou
trouvé = faux
indice = 0
_Pour_ i _allant de_ 1 à longueur de T
    _si_ T[i] modulo 2 == 0 et trouvé == faux
        alors 
              trouvé = vrai
              indice = i
_Sortie :_ afficher i
```
## exercice 26 [(chapitre 2 teams)](https://teams.microsoft.com/_#/school/ClassNotebook/G%C3%A9n%C3%A9ral?threadId=19:HSHKfbWjr9-G7aq6YrMXDaGG3IgxQCmAilRAEEfGofw1@thread.tacv2&ctx=channel&isTeamLevelApp=true) :
algorithme tableau trié :
```
_Données :_ une suite d'entier T // stockée dans un tableau
_Résultat :_ vrai si le tableau est trié, sinon, faux
trié = faux
_Pour_ i de 1 _à_ longueur de T - 1
    si T[i] < t[i+1]
    _alors_ trié = vrai _sinon_ trié = faux
afficher trié
```