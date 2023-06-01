from csv import reader
from time import sleep 

def ouvrirCsv(csvName: str) -> list:
    fichier: object = open(csvName)
    donnee: object = reader(fichier)
    tableauDonnee: list = []
    for ligne in donnee:
        tableauDonnee.append(ligne)
    return tableauDonnee

def triParInsertion(tableau: list) -> list:
    for i in range(1, len(tableau)):
        valeur: int = tableau[i]
        position: int = i

        while position > 0 and tableau[position - 1] > valeur:
            tableau[position], tableau[position - 1] = tableau[position - 1], tableau[position]
            position -= 1

    return tableau

def obtenirEchelleKnn(tableauDuCsv: list):
    tableauPourTriParInsertion: list = []
    resultatsTriParInsertion: int = 0
    resultatsEchelle: list = [[0] * (len(tableauDuCsv[0]) - 1) for _ in range(len(tableauDuCsv) - 1)]
    iteration: int = 0
    for colonnes in range(len(tableauDuCsv[0]) - 1):
        for lignes in range(1, len(tableauDuCsv)):
            print(lignes)
            tableauPourTriParInsertion.append(float(tableauDuCsv[lignes][colonnes]))

        resultatsTriParInsertion = triParInsertion(tableauPourTriParInsertion)[-1]
        
        for lignes in range(1, len(tableauDuCsv)):
            resultatsEchelle[lignes - 1][colonnes] = (float(tableauDuCsv[lignes][colonnes]) / resultatsTriParInsertion)
        print(resultatsEchelle)

def compteurEspece(tableauDuCsv: list, indiceEspece: int) -> list:
    sauvegarde: str = ""
    compteur: int = 0
    tableauEspece: list = []
    for ligne in range(len(tableauDuCsv)):
        if sauvegarde != tableauDuCsv[ligne][indiceEspece]:
            indice: int = ligne
            tableauEspece.append([compteur, ligne])
            compteur = 0
        compteur += 1
    return tableauEspece



"""
def obtenirMoyennePourEspece(tableauDuCsv: list):
   echelle: list = obtenirEchelleKnn(tableauDuCsv)
    tableauEspece: list = compteurEspece(tableauDuCsv, 4)
    moyenneEspece: list = []

    for espece in range(len(tableauEspece)):
        for occurenceEspece in range(tableauEspece[espece][0]):
            for colonnes in range(len(tableauDuCsv[0])):
                pass
"""
            
csvIris: list = ouvrirCsv("iris.csv")

obtenirEchelleKnn(csvIris)