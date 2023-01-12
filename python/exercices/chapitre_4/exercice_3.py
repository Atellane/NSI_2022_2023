userText: str = input("Entrer un texte pour connaitre la fréquence d'apparition de chaque lettres de l'alphabet dans cet texte :\n")

try :
	int(userText)
	print("PAS DE CHIFFRES :(((")
except ValueError :
	alphabetLetter: list = [chr(i) for i in range(65,91)]

	for i in alphabetLetter:
		nombreApparition: int = 0
		for j in userText:
			if j.upper() == i:
				nombreApparition +=1
		result: dict = {f"{i}": nombreApparition}
		print(f"{i} est apparut {result[i]} fois.")