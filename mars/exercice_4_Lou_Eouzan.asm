.data
somme: .byte 0
i: .byte 10
.text
#$t0 stocke la valeur de somme
lb $t0, somme
#$t1 stocke la valeur de i
lb $t1, i

for:
#va à fin si i==0
beqz $t1, fin
#additionne somme et i
add $t0, $t0, $t1
#soustraict 1 a i
sub $t1, $t1, 1
j for

fin:
#lignes pour afficher somme
li $v0, 1
add $a0, $t0, 0
syscall
#fin de lignes pour afficher somme
li $v0, 10
syscall
