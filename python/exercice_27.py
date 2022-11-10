# n : int
n = int(input("entrer un entier positif :\n"))
"""calcule la valeur d'un nombre 'p' compris dans l'intervale [ 0 ; n+1 ["""
for i in range(n+1) :
    # p : int
    p = i**2
    print(f"le nombre p vaut : {p}")