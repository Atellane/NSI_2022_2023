def sapin(nombreDeLignes: int) -> int:
	sapin = 1 + nombreDeLignes - 1 * 2
	pointSapin = sapin * "."
	chapeauxSapin = "^"

	for i in range(nombreDeLignes) :
		print(pointSapin + chapeauxSapin + pointSapin)
		pointSapin = pointSapin[:-1]
		chapeauxSapin += "^^"

tailleSapin = int(input("De quelle taille doit-être votre sapin ?\n"))
sapin(tailleSapin)