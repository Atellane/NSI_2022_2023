def maximumAndMinimumInAnArray(array: list) -> int :
	tableauClassement: list = []
	for i in range(len(array)):
		if len(tableauClassement) != 0:
			if tableauClassement[- 1] < array[i]:
				tableauClassement.append(array[i])
			elif tableauClassement[0] > array[i]:
				tableauClassement.insert(0, array[i])
			else:
				tableauClassement.insert(round(len(array)) / 2 - 1, array[i])
		else:
			tableauClassement.append(array[i])
	minimum: int = tableauClassement[0]
	maximum: int = tableauClassement[-1]
	tableauResultat: list = [minimum, maximum]
	return tableauResultat

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
	else:
		print(maximumAndMinimumInAnArray(tableau))