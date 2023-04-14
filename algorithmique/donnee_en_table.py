from csv import reader

def triParInsertion(tableau: list)-> list:
    for i in range(1, len(tableau)):
        valeur: str = tableau[i]
        position: int = i

        while position > 0 and tableau[position - 1] > valeur:
            tableau[position], tableau[position - 1] = tableau[position - 1], tableau[position]
            position -= 1

    return tableau

fichierCine: object = open("liste_des_cinemas.csv")
donneeCine: object = reader(fichierCine)
tableauDonnee: list = []
for ligne in donneeCine:
    donneeRecup: str = ligne[0].split(";")
    tableauDonnee.append(donneeRecup)

listeCineArtEtEssai: list = []
for i in range(len(tableauDonnee)):
    if (tableauDonnee[i][7] == "OUI"):
        listeCineArtEtEssai.append(tableauDonnee[i][1])
print(triParInsertion(listeCineArtEtEssai))
print("nombre de ciné d'art et d'essai :", len(listeCineArtEtEssai))

print("---------------------------------------------------------------------------------------")

listeCineArtEtEssaiAvecEcran3d: list = []
for i in range(len(tableauDonnee)):
    if (tableauDonnee[i][7] == "OUI" and tableauDonnee[i][8] == "OUI"):
        listeCineArtEtEssaiAvecEcran3d.append(tableauDonnee[i][1])
print(triParInsertion(listeCineArtEtEssaiAvecEcran3d))
print("nombre de ciné d'art et d'essai avec un écran 3d :", len(listeCineArtEtEssaiAvecEcran3d))

print("---------------------------------------------------------------------------------------")

listeCineParis: list = []
for i in range(len(tableauDonnee)):
    if ("Paris " in tableauDonnee[i][5]): # espace à "Paris " afins d'exclure les communes dont le nom contient "Paris" mais qui ne sont pas Paris
        listeCineParis.append(tableauDonnee[i][5])
print("nombre de ciné à Paris :", len(listeCineParis))
