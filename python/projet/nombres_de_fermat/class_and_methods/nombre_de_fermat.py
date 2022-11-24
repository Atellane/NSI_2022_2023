from math import sqrt
class NombreDeFermat() :
    def __init__(self, indice: int) -> None :
        """indiquer le nombre qu'on va traiter"""
        self.indice = indice

    def nombres_de_fermat(self) -> int :
        """calcule la valeur des nombres de fermat en fonction d'un indice donné à l'instenciation de la class"""
        Fermat: int = 2**(2**self.indice) + 1
        return Fermat
    
    def nombre_de_fermat_premier(self, nombre: int) -> None :
        """vérifie si un nombre de fermat est premier"""
        i: int = 2
        test_prealable: int = nombre % i
        if test_prealable != 0 :
            i = i + 1
            while i < sqrt(nombre) and nombre % i != 0:
                i = i + 2

            if i >= sqrt(nombre) :
                print(f"le nombre 2^(2^{self.indice}) + 1 (= {nombre}) est premier !")
            else :
                print(f"le nombre 2^(2^{self.indice}) + 1 (= {nombre}) n'est pas premier !")

        elif self.indice == 2 :
            print(f"le nombre 2^(2^{self.indice}) + 1 (= {nombre}) est premier !")
        else:
            print(f"le nombre 2^(2^{self.indice}) + 1 (= {nombre}) n'est pas premier !")
