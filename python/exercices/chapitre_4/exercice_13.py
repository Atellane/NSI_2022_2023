from random import randint
def obtenirResultatExamen(note: int) -> str:
	if note < 10:
		resultat: str = "Éliminé !!"
	elif note < 12:
		resultat: str = "Passable !"
	elif note < 14:
		resultat: str = "Assez Bien."
	elif note < 16:
		resultat: str = "Bien !"
	else:
		resultat: str  = "Très Bien !!"

	return resultat

assert obtenirResultatExamen(9) == "Éliminé !!", "ça fonctionne pas pour note < 10"
assert obtenirResultatExamen(11) == "Passable !", "ça fonctionne pas pour note < 12"
assert obtenirResultatExamen(13) == "Assez Bien.", "ça fonctionne pas pour note < 14"
assert obtenirResultatExamen(15) == "Bien !", "ça fonctionne pas pour note < 16"
assert obtenirResultatExamen(20) == "Très Bien !!", "ça fonctionne pas pour note >= 15"

for i in range(20):
	print(obtenirResultatExamen(randint(0,20)))