def construireTrianglePascal(nombreDeLignes: int) -> None :
	nombreInitial: int = 1
	tableau: list = [[nombreInitial]]
	if nombreDeLignes != 1:
		for i in range(1, nombreDeLignes):
			tableau.append([])
			for k in range(len(tableau[i - 1]) + 1):
				try:
					if k != 0:
						tableau[i].append(tableau[i - 1][k - 1] + tableau[i - 1][k])
					else:
						tableau[i].append(1)
				except IndexError:
					tableau[i].append(1)

	def afficherTriangleDePascal(tableau: list, nombreDeLignes: int) -> None:
		for i in range(nombreDeLignes):
			for k in range(len(tableau[i])):
				if k != len(tableau[i]) - 1:
					print(tableau[i][k], end = " ")
				else:
					print(tableau[i][k])
	if nombreDeLignes != 0:
		afficherTriangleDePascal(tableau, nombreDeLignes)

try:
	nombreDeLignes = int(input("entrer le nombre de ligne du triangle de Pascal à faire apparaitre :\n"))
except ValueError:
	raise ValueError("Seul les nombres sont acceptés pour le nombre de lignes")

construireTrianglePascal(nombreDeLignes)