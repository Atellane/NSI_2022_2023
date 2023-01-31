def start() -> None:
    mot: str = input("Joueur 1 : \nrentrer le mot que le joueur 2 devra deviner : \n")
    affichageMot: list = []
    for i in range(len(mot)):
        affichageMot.append("_")
    erreur: int = 0

    def afficherPendu(nombreErreur: int) -> None:
        pendu_final = []
        pendu_final.append(" --------------")
        pendu_final.append("   |        |")
        pendu_final.append("   |        |")
        pendu_final.append("   |       / \\")
        pendu_final.append("   |       \\_/")
        pendu_final.append("   |      __|__")
        pendu_final.append("   |        |")
        pendu_final.append("   |        |")
        pendu_final.append("   |       / \\")
        pendu_final.append("  /|\\     /   \\")
        pendu_final.append(" / | \\")
        pendu_final.append("/  |  \\")
        pendu_final.append("~~~~~~~~~~~~~~~~~~~~~")
        pendu_final.append("~~~~~~~~~~~~~~~~~~~~~")
        pendu_final.append("~~~~~~~~~~~~~~~~~~~~~")
        pendu_final.append("~~~~~~~~~~~~~~~~~~~~~")
        for i in range(2*nombreErreur):
            print(pendu_final[i])

    while erreur < 8:
        propositionMot: str = input("entrer une lettre :\n")
        if propositionMot in mot:
            for i in range(len(mot)):
                if propositionMot == mot[i]:
                    affichageMot[i] = mot[i]
            print(f"Bravo ! \nVous avez fait {erreur} erreur(s) sur 8 erreurs autorisées.")
            afficherPendu(erreur)
            for i in range(len(affichageMot)):
                print(affichageMot)
        else:
            erreur += 1
            print(f"Dommage ! \nVous avez fait {erreur} erreur(s) sur 8 erreurs autorisées.")
            afficherPendu(erreur)
            for i in range(len(affichageMot)):
                print(affichageMot[i])

start()