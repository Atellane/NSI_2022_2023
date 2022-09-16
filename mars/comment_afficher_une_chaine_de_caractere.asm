.data

string: .asciiz "Hello world !"
.text

# pour afficher une chaine de caractère je fais :
addi $v0, $zero, 4
la $a0, string
syscall
# fin de l'affichage de la chaine de caractère
li $v0, 10
syscall

