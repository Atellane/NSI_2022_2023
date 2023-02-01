def aficherToutLesNombresSaufCeuxQuiContiennentN(n: int, nombreMaxi: int) -> None:
	n = str(n)
	for i in range(nombreMaxi + 1):
		i = str(i)
		if n not in i:
			print(i, end = " ")
n: int = int(input("Choisir un chiffre n pour lequel tous les nombres le contenant ne seront pas afficher :\n"))
nombreMaxi: int = int(input("Choisir un nombre maximum qui sera le dernier nombre afficher :\n"))

aficherToutLesNombresSaufCeuxQuiContiennentN(n, nombreMaxi)