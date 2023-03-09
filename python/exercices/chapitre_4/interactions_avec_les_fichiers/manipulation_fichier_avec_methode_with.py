with open("texte_a_lire.txt", "rt") as texteALire:
    for ligne in texteALire:
        print(ligne, end="")

with open("texte_a_ecrire.txt", "wt") as fichierTexteAEcrire:
    texteAEcrire: str = input("Entrer le texte que vous souhaitez voire apparaitre dans votre fichier (si vous souhaitez aller à la ligne utilisez \"\\n\") :\n") 
    fichierTexteAEcrire.write(f"{texteAEcrire}")

with open("texte_a_ecrire.txt", "rt"):
    print(f"Vous avez écris ceci dans votre fichier :")
    for ligne in fichierTexteAEcrire:
        print(ligne, end="")

