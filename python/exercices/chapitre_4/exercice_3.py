def decompteLettres(userText: str) -> dict:
	try :
		int(userText)
		print("PAS DE CHIFFRES :(((")
	except ValueError :
		alphabetLetter: list = [chr(i) for i in range(65,91)]

		result: dict = {}

		for i in alphabetLetter:
		  nombreApparition: int = 0
		  for j in userText:
		    if j.upper() == i:
		      nombreApparition +=1
		    result[f"{i.upper()}"] = nombreApparition
		return result

userText: str = input("Entrer un texte pour connaitre la fréquence d'apparition de chaque lettres de l'alphabet dans cet texte :\n")
print(decompteLettres(userText))