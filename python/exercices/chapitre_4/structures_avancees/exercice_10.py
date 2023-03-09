from getpass import getpass
def decompteLettres(userText: str, lettreATrouver: str) -> dict:
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
    return result[f"{lettreATrouver.upper()}"]

def start() -> None:
    mot: str = getpass("Joueur 1 : \nrentrer le mot que le joueur 2 devra deviner : \n")
    affichageMot: list = []
    for i in range(len(mot)-2):
      affichageMot.append("_")
    affichageMot.insert(0, mot[0])
    affichageMot.append(mot[-1])
    print("trouver les lettres du mots suivant :", end=" ")
    for i in range(len(affichageMot)):
      print(affichageMot[i], end=" ")
    print("\n")
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
      if "_" not in affichageMot:
        print("Bravo, vous avez gagné.e !")
        exit()

      propositionMot: str = input("entrer une lettre :\n")
      if len(propositionMot) > 1:
        print("1 lettre à la fois, pas un mot entier...")
        continue
      if propositionMot in mot and propositionMot not in affichageMot:
        for i in range(len(mot)):
          if propositionMot == mot[i]:
            affichageMot[i] = mot[i]
          print(f"Bravo ! \nVous avez fait {erreur} erreur(s) sur 8 erreurs autorisées.")
          afficherPendu(erreur)
          for i in range(len(affichageMot)):
            print(affichageMot[i], end=" ")
          print("\n")
      elif propositionMot in affichageMot:
        emplacementAffichageMot: int = 0
        for lettre in affichageMot:
          if lettre == propositionMot:
            if decompteLettres(mot, propositionMot) < decompteLettres(affichageMot[emplacementAffichageMot], lettre):
              print(f"Bravo ! \nVous avez fait {erreur} erreur(s) sur 8 erreurs autorisées.")
              afficherPendu(erreur)
              for i in range(len(affichageMot)):
                print(affichageMot[i], end=" ")
              print("\n")
              emplacementAffichageMot += 1
        if not decompteLettres(mot, propositionMot) < decompteLettres(affichageMot[emplacementAffichageMot], lettre):
          erreur += 1
          print(f"Dommage, vous aviez déjà donné cette lettre ! \nVous avez fait {erreur} erreur(s) sur 8 erreurs autorisées.")
          afficherPendu(erreur)
          for i in range(len(affichageMot)):
            print(affichageMot[i], end=" ")
          print("\n")
          
      elif proposition:
        erreur += 1
        print(f"Dommage, vous aviez déjà donné cette lettre ! \nVous avez fait {erreur} erreur(s) sur 8 erreurs autorisées.")
        afficherPendu(erreur)
        for i in range(len(affichageMot)):
          print(affichageMot[i], end=" ")
          print("\n")
      else:
        erreur += 1
        print(f"Dommage ! \nVous avez fait {erreur} erreur(s) sur 8 erreurs autorisées.")
        afficherPendu(erreur)
        for i in range(len(affichageMot)):
          print(affichageMot[i], end=" ")
          print("\n")

    if erreur == 8:
      print("Dommage, vous avez perdu.e !")
      exit()


start()