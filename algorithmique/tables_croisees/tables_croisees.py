from csv import reader

def ouvrirCsv(csvName: str) -> list:
    fichier: object = open(csvName)
    donnee: object = reader(fichier)
    tableauDonnee: list = []
    for ligne in donnee:
        tableauDonnee.append(ligne)
    return tableauDonnee

empruntCsv: list = ouvrirCsv("Emprunts.csv")

listeIdEmprunts2011: list = [empruntCsv[i][2] for i in range(len(empruntCsv)) if (empruntCsv[i][1] == "2011")]

romansCsv: list = ouvrirCsv("Romans.csv")

listeEmprunts2011: list = [romansCsv[i][1] for i in range(len(romansCsv)) for k in range(len(listeIdEmprunts2011)) if (romansCsv[i][0] == listeIdEmprunts2011[k])]

print("Les romans empruntés en 2011 sont :")
for i in listeEmprunts2011:
    print(i)

print("--------------------------------------------------------------------------------------------------------------------------------------------------------")

prixLitteraireCsv: list = ouvrirCsv("PrixLitteraire.csv")

idRomansPrixLitteraire2013: list = [prixLitteraireCsv[i][2] for i in range(len(prixLitteraireCsv)) if (prixLitteraireCsv[i][3] == "2013")]

idAuteurRomansPrixLitteraire2013: list = [romansCsv[i][2] for i in range(len(romansCsv)) for k in range(len(idRomansPrixLitteraire2013)) if (romansCsv[i][0] == idRomansPrixLitteraire2013[k])]

auteursCsv: list = ouvrirCsv("Auteurs.csv")

auteurPrixLitteraire2013: list = [auteursCsv[i][1] for i in range(len(auteursCsv)) for k in range(len(idAuteurRomansPrixLitteraire2013)) if (auteursCsv[i][0] == idAuteurRomansPrixLitteraire2013[k])]

print("Les auteur.ice.s aillant eu un/des prix en 2013 sont :")
for i in auteurPrixLitteraire2013:
    print(i)

print("--------------------------------------------------------------------------------------------------------------------------------------------------------")

listeEmprunts2012: list = [[empruntCsv[i][2], empruntCsv[i][3]] for i in range(len(empruntCsv)) if (empruntCsv[i][1] == "2012")]

for i in range(len(listeEmprunts2012)):
    listeEmprunts2012[i][0] = [romansCsv[i][1] for k in range(len(romansCsv)) if (listeIdEmprunts2011[i][0] == romansCsv[k][0])][0]

print("Les romans empruntés en 2012 sont :")
for i in listeEmprunts2012:
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------")
    print(f"{i[0]} (a été emprunté {i[1]} fois)")

print("--------------------------------------------------------------------------------------------------------------------------------------------------------")

idAntoineDeSaintExupery: str = ""
for i in auteursCsv:
    if i[1] == "Antoine de Saint-Exupéry":
        idAntoineDeSaintExupery = i[0]

romansSaintExuperyQuiOntPasRecuDePrix: list = [[romansCsv[i][1], romansCsv[i][0]] for i in range(len(romansCsv)) if romansCsv[i][2] == idAntoineDeSaintExupery]

romansSaintExuperyQuiOntRecuUnPrix: list = [[romansSaintExuperyQuiOntPasRecuDePrix[i][0], romansSaintExuperyQuiOntPasRecuDePrix[i][1]] for i in range(len(romansSaintExuperyQuiOntPasRecuDePrix)) for k in range(len(prixLitteraireCsv)) if romansSaintExuperyQuiOntPasRecuDePrix[i][1] == prixLitteraireCsv[k][2]]

for i in romansSaintExuperyQuiOntRecuUnPrix:
    romansSaintExuperyQuiOntPasRecuDePrix.remove(i)

print("--------------------------------------------------------------------------------------------------------------------------------------------------------")

print("Les romans écrit par Antoine de Saint-Exupéry sont (ils ont tous reçus un prix) :")
for i in romansSaintExuperyQuiOntRecuUnPrix:
    print(i[0])

print("--------------------------------------------------------------------------------------------------------------------------------------------------------")

listeEmprunts2014: list = [[empruntCsv[i][2], empruntCsv[i][3]] for i in range(len(empruntCsv)) if (empruntCsv[i][1] == "2014")]

idRomanPlusEmprunte2014: str = ""
for i in listeEmprunts2014:
    nombreEmpruntMax: int = 0
    if (int(i[1]) > nombreEmpruntMax):
        nombreEmpruntMax = i[1]
        idRomanPlusEmprunte2014 = i[0]

titreEtIdAuteurRomanPlusEmprunte2014: list = [[romansCsv[i][1], romansCsv[i][2]] for i in range(len(romansCsv))if (romansCsv[i][0] == idRomanPlusEmprunte2014)]

auteurRomanPlusEmprunte2014: str = ""
for i in range(len(auteursCsv)):
    for k in titreEtIdAuteurRomanPlusEmprunte2014:
        if (auteursCsv[i][0] == k[1]):
            auteurRomanPlusEmprunte2014 = auteursCsv[i][1]


idRomanDominiqueDeSaintMars: list = [romansCsv[i][0] for i in range(len(romansCsv)) if (romansCsv[i][2] == titreEtIdAuteurRomanPlusEmprunte2014[0][1])]

prixLitteraireOuNon2014: str = "cet auteur n'as pas reçu de prix littéraire"
for i in prixLitteraireCsv:
    for k in idRomanDominiqueDeSaintMars:
        if (i[2] == k):
            prixLitteraireOuNon2014 = "cet auteur a reçu un prix littéraire"

print(f"Le roman le plus emprunté de 2014 a pour titre \"{titreEtIdAuteurRomanPlusEmprunte2014[0][0][:-1]}\", pour auteur \"{auteurRomanPlusEmprunte2014[1:]}\" et {prixLitteraireOuNon2014}.")