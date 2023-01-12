from random import randint
def validityTestScrabble(stringToTest: str) -> str :
	voyelles: list = ["A", "E", "I", "O", "U", "Y"]
	consonnes: list = [chr(i) for i in range(65,91) if chr(i) not in voyelles]
	compteurVoyelles: int = 0
	compteurConsonnes: int = 0

	invalidBecauseOfLetters: str = f"Votre chaine {stringToTest} est invalide, elle ne peut contenir que des lettres :("
	invalidBecauseOfLength: str = f"Votre chaine {stringToTest} est invalide, elle doit contenir au moins 7 lettres ;)"
	invalidBecauseOfVoyellesOrConsonnes: str = f"Votre chaine {stringToTest} est invalide, elle doit contenir au moins 2 consonnes et 2 voyelles :/"
	valid: str = f"Votre chaine {stringToTest} est valide :)"

	if len(stringToTest) >= 7 :
		for i in stringToTest :
			try :
				int(i)
				return invalidBecauseOfLetters
			except ValueError :
				for j in voyelles :
					if i == j:
						compteurVoyelles += 1
				for j in consonnes:
					if i == j:
						compteurConsonnes += 1
		if compteurVoyelles < 2 or compteurConsonnes < 2 :
			return invalidBecauseOfVoyellesOrConsonnes
		else:
			return valid
	else:
		return invalidBecauseOfLength

assert validityTestScrabble("12345678") == "Votre chaine 12345678 est invalide, elle ne peut contenir que des lettres :(", "l'erreur empéchant d'utiliser des lettres ne fonctionne pas"
assert validityTestScrabble("azerty") == "Votre chaine azerty est invalide, elle doit contenir au moins 7 lettres ;)", "l'erreur exigeant 7 lettres ne fonctionne pas"
assert validityTestScrabble("pqrstuvwx") == "Votre chaine pqrstuvwx est invalide, elle doit contenir au moins 2 consonnes et 2 voyelles :/", "l'erreur exigeant 2 consonnes et 2 voyelles ne fonctionne pas"

longueurMot = randint(7, 20)
mot = ""
for i in range(1,longueurMot):
	mot = mot + chr(randint(65,90))
print(validityTestScrabble(mot))