def obtenirNombresNonMultipleDUnEnrierNonNul(entierNonNul: int, listeDansLaquelleChercher: list) -> list:
	if entierNonNul != 0:
		listeResultat: list = [i for i in listeDansLaquelleChercher if i % entierNonNul != 0]
		return listeResultat
	else:
		print("Seul les entiers NON NULS sont acceptés, merci de votre compréhension")

def demandeEntierNonNulUtilisateur() -> int:
	while True:
		entierNonNul: str = input("Entrez un entier non nul :\n")
		try:
			entierNonNul: int = int(entierNonNul)
			return entierNonNul
		except ValueError:
			print("seul les chiffres sont acceptés !")


def demandeTableauUtilisateur() -> list:
	tableau: list = []
	demandeValeurTableau: str = ""
	while demandeValeurTableau != "fini":
		demandeValeurTableau = input("Entrer une valeur à ajouter au tableau, taper 'fini' quand vous avez teminé :\n")
		if demandeValeurTableau != "fini":
			try :
				valeurTableau: int = int(demandeValeurTableau)
				tableau.append(valeurTableau)
			except ValueError :
				print("seul les chiffres sont acceptés !")
		else :
			return tableau

def supprimerRepetitionDansUnTableau(array: list) -> list:
	tableau: list = array.copy()
	for i in range(len(array) - 1, -1, -1):
		compteur: int = 0
		for k in range(len(array)):
			if array[i] == array[k]:
				compteur +=1
		if compteur > 1:
			del tableau[i]
	return tableau

entierNonNul: int = demandeEntierNonNulUtilisateur()

listeDansLaquelleChercher: list = demandeTableauUtilisateur()
listeDansLaquelleChercher: list = supprimerRepetitionDansUnTableau(listeDansLaquelleChercher)

listeResultat: list = obtenirNombresNonMultipleDUnEnrierNonNul(entierNonNul, listeDansLaquelleChercher)
print(listeResultat)

print(f"liste des entiers de la liste {listeDansLaquelleChercher} qui ne sont pas multiple de {entierNonNul} :")
for i in range(len(listeResultat)):
	print(f"{i} : {listeResultat[i]}")