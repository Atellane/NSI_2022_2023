from class_fonction.fonction_class import partie1, arithmetique, chaine_de_caractere

partie1() # calcul m*x+p (m, x et p sont donné par l'utilisateur.ice)

partie2 = arithmetique("2") # crée une instance 'partie2' de la class arithmetique avec self.name = "2."

# affiche le nom de l'instance de arithmetique et donne le quotient de la division euclidienne 42/5
print(partie2.name)
partie2.divisionEuclidienne("quotient", 42, 5)

partie3 = arithmetique("3") # crée une instance 'partie3' de la class arithmetique avec self.name = "3."

# affiche le nom de l'instance de arithmetique et donne le reste de la division euclidienne 42/5
print(partie3.name)
partie3.divisionEuclidienne("reste", 42, 5)

partie4 = arithmetique("4") # crée une instance 'partie4' de la class arithmetique avec self.name = "4."

# affiche le nom de l'instance de arithmetique et donne le résultat de la division rélle 42.0/5.0
print(partie4.name)
partie4.divisionReelle(42.0, 5.0)

partie5 = arithmetique("5") # crée une instance 'partie5' de la class arithmetique avec self.name = "5."

# affiche le nom de l'instance arithmetique et teste l'égalité de 6 et 2 * 3
print(partie5.name)
partie5.testEgalite(6, 2, 3)

partie6 = chaine_de_caractere("6") # crée une instance 'partie 6' de la class chaine_de_caractere avec self.name = "6."

# affiche le nom de l'instance chaine_de_caractere et concatène les 2 chaine de caractères que sa méthode concatenation prend en paramètre
print(partie6.name)
partie6.concatenation("j'aprends ", "la programmation dite 'impérative'")

partie7 = chaine_de_caractere("7") # crée une instance 'partie 7' de la class chaine_de_caractere avec self.name = "7.

# affiche le nom de l'instance chaine_de_caractere et affiche la chaine de caractères que sa méthode afficher prend en paramètre
print(partie7.name)
partie7.afficher("Bonjour!")

partie8 = chaine_de_caractere("8") # # crée une instance 'partie 8' de la class chaine_de_caractere avec self.name = "8."

# affiche Le nom de l'instance de chaine_de_caractere, demande son prénom à l'utilisateur et affiche 'Bonjour' suivit du prénom de l'utilisateur
print(partie8.name)
partie7.prenom()

partie9 = arithmetique("9") # crée une instance 'partie5' de la class arithmetique avec self.name = "5."

# affiche le nom de l'instance de arithmetique, calule l'âge de l'utilisateur à partir de son année de naissance, puis l'affiche
print(partie9.name)
partie9.age()