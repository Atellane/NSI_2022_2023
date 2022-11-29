from class_and_methods.nombre_de_fermat import NombreDeFermat
from time import sleep
"""
crée une instance 'testNombreFermat' de la class 'NombreDeFermat' avec 'self.indice = 3' 
et vérifie si l'image de 3 par la fonction qui donne les nombres de Fermat est première ou non
"""
for i in range(6) :
    testNombreFermat: object = NombreDeFermat(i)
    testNombreFermat.nombre_de_fermat_premier(testNombreFermat.nombres_de_fermat())

sleep(5.0)

for i in range(32) :
    calculNombreFermat: object = NombreDeFermat(i)
    print(calculNombreFermat.nombres_de_fermat(), "\n")
