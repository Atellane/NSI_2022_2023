from temperature.conversions import convertir_temperature

"""
crée une instance 'testFarhenheitEnCelsius' de la class 'convertir_temperature' puis vérifie que la méthode 'farhenheitEnCelsius'
retourne bien la valeur 37,777777777777778 quand on lui donne la valeur 100 et affiche 'oups, ça marche pas :((' si ce n'est pas
le cas
"""
testFarhenheitEnCelsius = convertir_temperature("Conversion de degré farhenheit en degré celsius")
assert testFarhenheitEnCelsius.farhenheitEnCelsius(100) == 37.777777777777778, "oups, ça marche pas :(("

"""
crée une instance 'testCelsiusEnFarhenheit' de la class 'convertir_temperature' puis vérifie que la méthode 'celsiusEnFarhenheit'
retourne bien la valeur 68 quand on lui donne la valeur 20 et affiche 'MAIS TU VAS MARCHER OUI OU ZUT ? ;-;' si ce n'est pas
le cas
"""
testCelsiusEnFarhenheit = convertir_temperature("Conversion de degré celsius en degré farhenheit")
assert testCelsiusEnFarhenheit.celsiusEnFarhenheit(20) == 68, "MAIS TU VAS MARCHER OUI OU ZUT ? ;-;"