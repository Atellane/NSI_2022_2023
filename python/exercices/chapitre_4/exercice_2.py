tableau: list = []
demandeValeurTableau: str = ""
while demandeValeurTableau != "fini":
	demandeValeurTableau = input("Entrer une valeur à ajouter au tableau, taper 'fini' quand vous avez teminé :\n")
	if demandeValeurTableau != "fini":
		valeurTableau: int = int(demandeValeurTableau)
		tableau.append(valeurTableau)
	else:
		for i in range(1, len(tableau)):
			print(f"for {i = } : {tableau[i] = }")