def obtenirListeTriplets(partieExo: int) -> list:
	n: int = int(input("Entrer un chiffre :\n"))
	if partieExo == 1:
		liste: list = [(i, j, k) for i in range(1, n+1) for j in range(1, n+1) for k in range(1, n+1)]
	elif partieExo == 2:
		liste: list = [(i, j, k) for i in range(1, n+1) for j in range(1, n+1) for k in range(1, n+1) if i+j == k]
	elif partieExo == 3:
		liste: list = [(i, j, k) for i in range(1, n+1) for j in range(1, n+1) for k in range(1, n+1) if i <= j <= k]
	else:
		print("Ça existe pas patate...")
	return liste


print(obtenirListeTriplets(3))