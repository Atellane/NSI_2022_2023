def sontAnagrammes(mot1: str, mot2: str) -> bool:
	compteurLettresIdentiques: int = 0
	mot1 = mot1.upper()
	mot2 = mot2.upper()
	if len(mot1) != len(mot2):
		return False
	else:
		for i in range(len(mot1)):
			for j in range(len(mot2)):
				if mot1[i] == mot2[j]:
					compteurLettresIdentiques += 1
		if compteurLettresIdentiques == len(mot1):
			return True
		else:
			return False

assert sontAnagrammes("Lou", "Uol") == True, "C'est pas bon"

assert sontAnagrammes("Lou", "Uole") == False, "C'est pas bon"

assert sontAnagrammes("Lou", "Liv") == False, "C'est pas bon"

mot1: str = input("Entrer un mot :\n")
mot2: str = input("Entrer un autre mot pour savoir si c'est l'anagramme du premier :\n")

if sontAnagrammes(mot1, mot2):
	print(f"{mot2} est un anagramme de {mot1} (ou l'inverse d'ailleurs) :)")
else:
	print(f"{mot2} n'est pas un anagramme de {mot1} :(")