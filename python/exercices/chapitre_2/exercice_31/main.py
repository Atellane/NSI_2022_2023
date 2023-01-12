from fonctions_polynomiale.fonctions import fonction1, fonction2

"""vérifie que les fonction fonction1 et fonction2 renvoies bien la bonne valeur si tous leurs paramètre valent 2"""
assert fonction1(2, 2, 2, 2, 2) == 30, "la fonction 1 fonctionne pas"
assert fonction2(2, 2, 2, 2) == 42, "la fonction 2 fonctionne pas"
