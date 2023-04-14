def obtenirTableau() -> list:
    nombreCaseTableau: int = int(input("Combien de cases voulez-vous donner à votre tableau ?\n"))
    tableau: list = []
    for i in range(0, nombreCaseTableau):
        tableau.append(input(f"Quel valeur doit avoir la case n°{i + 1} ?\n"))
        print(f"La valeur n°{i + 1} de votre tableau vaut {tableau[i]}")
    
    return tableau

def triParInsertion(tableau: list)-> list:
    for i in range(1, len(tableau)):
        valeur: int = tableau[i]
        position: int = i

        while position > 0 and tableau[position - 1] > valeur:
            tableau[position], tableau[position - 1] = tableau[position - 1], tableau[position]
            position -= 1

    return tableau

tableau: list = obtenirTableau()

print(triParInsertion(tableau))