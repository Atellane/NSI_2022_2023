def supprimerRepetitionDansUnTableau(array: list) -> list:
	tableau: list = array.copy()
	for i in range(len(array) - 1, -1, -1):
		compteur: int = 0
		for k in range(len(array)):
			if array[i] == array[k]:
				compteur +=1
				print(compteur)
		if compteur > 1:
			del tableau[i]
	return tableau

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
				tableau.append(valeurTableau)
		else :
			return tableau

print(supprimerRepetitionDansUnTableau(demandeTableauUtilisateur()))