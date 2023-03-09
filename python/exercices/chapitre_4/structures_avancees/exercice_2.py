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
				tableau.append(demandeValeurTableau)
		else :
			return tableau

test = demandeTableauUtilisateur()

for i in range(len(test)):
	print(f"{i} : {test[i]}")