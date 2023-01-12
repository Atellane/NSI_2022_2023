from class_and_methods.nombre_de_fermat import NombreDeFermat
from time import sleep
"""
crée une instance 'testNombreFermat' de la class 'NombreDeFermat' avec 'self.indice = i' 
et vérifie si l'image de i par la fonction qui donne les nombres de Fermat est première ou non pour
i ∈ [0 ; 5]
"""
for i in range(6) :
    testNombreFermat: object = NombreDeFermat(i)
    testNombreFermat.nombre_de_fermat_premier(testNombreFermat.nombres_de_fermat())

sleep(5.0)

"""
crée une instance 'calculNombreFermat' de la class 'NombreDeFermat' avec 'self.indice = i' 
et calcule l'image de i par la fonction qui donne les nombres de Fermat pour i ∈ [0 ; 5]
"""
for i in range(32) :
    calculNombreFermat: object = NombreDeFermat(i)
    print(calculNombreFermat.nombres_de_fermat(), "\n")