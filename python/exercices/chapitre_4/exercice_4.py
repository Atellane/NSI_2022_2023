from random import randint
def validityTestScrabble(stringToTest: str) -> str :
	voyelles: list = ["A", "E", "I", "O", "U", "Y"]
	consonnes: list = [chr(i) for i in range(65,91) if chr(i) not in voyelles]
	compteurVoyelles: int = 0
	compteurConsonnes: int = 0

	invalidBecauseOfLetters: str = "Votre chaine est invalide, elle ne peut contenir que des lettres :("
	invalidBecauseOfLength: str = "Votre chaine est invalide, elle doit contenir au moins 7 lettres ;)"
	invalidBecauseOfVoyellesOrConsonnes: str = "Votre chaine est invalide, elle doit contenir au moins 2 consonnes et 2 voyelles :/"
	Valid = "Votre chaine est valide :)"

	if len(stringToTest) >= 7:
		for i in stringToTest :
			try :
				int(i)
				return invalidBecauseOfLetters
			except ValueError :
				if i in voyelles:
					compteurVoyelles += 1
				else:
					compteurConsonnes += 1
				if compteurVoyelles < 2 or compteurConsonnes < 2:
					return invalidBecauseOfVoyellesOrConsonnes
				continue
		return
	else:
		return invalidBecauseOfLength

 