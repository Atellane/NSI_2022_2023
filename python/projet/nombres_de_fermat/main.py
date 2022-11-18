from class_and_methods.nombre_de_fermat import ceNombreDeFermatEstIlPremier

"""
crée une instance 'testNombreFermat' de la class 'ceNombreDeFermatEstIlPremier' avec 'self.indice = 3' 
et vérifie si l'image de 3 par la fonction qui donne les nombres de Fermat est première ou non
"""
testNombreFermat: object = ceNombreDeFermatEstIlPremier(3)
testNombreFermat.nombre_de_fermat_premier(testNombreFermat.nombres_de_fermat())