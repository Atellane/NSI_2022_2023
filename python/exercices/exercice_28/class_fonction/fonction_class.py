from abc import ABC
def partie1() -> None :
    """définie une fonction qui calcule l'image de x pour fonctions affines """
    # name : str
    name = "1."
    print(name)
    # m : int
    m = 15
    # x : int
    x = 20
    # p : int
    p = 25
    resultat = m*x+p
    print(f"\n{m = }\n{x = }\n{p = }\nf(x) = mx+p\n    <=> {m} * {x} + {p}\n {m} * {x} + {p} = {resultat} \n")


class partie_exercice(ABC) :
    """permet d'instancier les différentes parties de l'exercice 28"""
    
    # name : str
    def __init__(self, name: str) -> None :
        self.name = name + "."

class arithmetique(partie_exercice) :
    def __init__(self, name: str) -> None :
        super().__init__(name)
    
    # quotient : str, dividende : int, diviseur : int
    def divisionEuclidienne(self, renvoie: str, dividende: int, diviseur: int) :
        """effectue une divison euclidienne de la valeur du paramètre dividende par la valeur du paramètre diviseur et renvoie le quotient ou le reste"""
        if renvoie == "quotient" :
            quotient = dividende // diviseur
            print(f"le quotient de la division euclidenne {dividende} / {diviseur} est {quotient}\n")
        elif renvoie == "reste" :
            reste = dividende % diviseur
            print(f"le reste de la division euclidenne {dividende} / {diviseur} est {reste}\n")
        else :
            print("écrire 'quotient' ou 'reste' en premier paramètre de la fonction\n")

    # dividende : float, dividende : float
    def divisionReelle(self, dividende: float, diviseur: float) -> None :
        """effectue une divison réelle de la valeur du paramètre dividende par la valeur du paramètre diviseur et renvoie le résultat"""
        resultat = dividende / diviseur
        print(f"le résultat de la division réelle {dividende} / {diviseur} est {resultat}\n")
    
    def testEgalite(self, x: int, y: int, z: int) -> None :
        """test l'égalité de deux valeur, affiche True si les deux valeurs sont égales, false si les deux valeurs ne le sont pas"""
        if x == y*z :
            print(f"{x} et {y} * {z} sont égaux\n")
        else :
            print(f"{x} et {y} * {z} ne sont pas égaux\n")
    
    def age(self) -> None :
        """donne l'âge de l'utilisateur en fonction de son année de naissance et l'affiche"""
        # annee : int
        annee = int(input("rentre ton année de naissance :\n"))
        # age : int
        age = 2022 - annee
        print(f"tu as {age} ans\n")

class chaine_de_caractere(partie_exercice) :
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def concatenation(self, str1: str, str2: str) -> None :
        """concatène (= assemble) 2 chaînes de caractère"""
        print(str1 + str2 + "\n")
    
    def afficher(self, chaineDeCaractere: str) -> None :
        """affiche une chaine de caractère"""
        print(chaineDeCaractere+ "\n")

    def prenom(self) -> None :
        prenom = input("entre ton prénom :\n")
        print(f"Bonjour {prenom} !\n")