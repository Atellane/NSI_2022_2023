nombreCaseTableau: int = int(input("Combien de cases voulez-vous donner à votre tableau ?\n"))
tableau: list = []
for i in range(0, nombreCaseTableau):
	tableau.append(input(f"Quel valeur doit avoir la case n°{i + 1} ?\n"))
	print(f"La valeur n°{i + 1} de votre tableau vaut {tableau[i]}")