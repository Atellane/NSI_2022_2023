from csv import reader
from time import sleep 
from matplotlib import pyplot as plt

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

def distance(x: float,y: float,z: float,t: float,a: float,b: float,c: float,d: float):
    """
    Renvoie la distance euclidienne entre les points de coordonnées In (x,y,z,t) et celui de coordonnées (a,b,c,d)"...
    """
    return sqrt((x-a)**2+(y-b)**2+(z-c)**2+(t-d)**2)

"""
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

#### Affichage des points ####

sepal_x_s = [csvIris[i][0] for i in range(len(csvIris)) if csvIris[i][4] == "Setosa"]
sepal_y_s = [csvIris[i][1] for i in range(len(csvIris)) if csvIris[i][4] == "Setosa"]
petal_x_s = [csvIris[i][2] for i in range(len(csvIris)) if csvIris[i][4] == "Setosa"]
petal_y_s = [csvIris[i][3] for i in range(len(csvIris)) if csvIris[i][4] == "Setosa"]
plt.plot(sepal_x_s, sepal_y_s, "ro")
sepal_x_v = [csvIris[i][0] for i in range(len(csvIris)) if csvIris[i][4] == "Versicolor"]
sepal_y_v = [csvIris[i][1] for i in range(len(csvIris)) if csvIris[i][4] == "Versicolor"]
petal_x_v = [csvIris[i][2] for i in range(len(csvIris)) if csvIris[i][4] == "Versicolor"]
petal_y_v = [csvIris[i][3] for i in range(len(csvIris)) if csvIris[i][4] == "Versicolor"]
plt.plot(sepal_x_v, sepal_y_v, "go")
sepal_x_V = [csvIris[i][0] for i in range(len(csvIris)) if csvIris[i][4] == "Virginica"]
sepal_y_V = [csvIris[i][1] for i in range(len(csvIris)) if csvIris[i][4] == "Virginica"]
petal_x_V = [csvIris[i][2] for i in range(len(csvIris)) if csvIris[i][4] == "Virginica"]
petal_y_V = [csvIris[i][3] for i in range(len(csvIris)) if csvIris[i][4] == "Virginica"]
plt.plot(sepal_x_V, sepal_y_V, "bo") 
plt.show()
plt.plot(petal_x_s, petal_y_s, "ro")
plt.plot(petal_x_v, petal_y_v, "go")
plt.plot(petal_x_V, petal_y_V, "bo")
plt.show()

# penser a regarder le fichier teams réponse algo plus proche voisins et adpater ce fichier