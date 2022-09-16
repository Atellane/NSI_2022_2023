.data
tab: .byte, 2, 23, 12, 3, 8, 1
s: .byte, 3
p: .byte, 8
line_break: .asciiz "\n"
.text
la $t0, tab
main:
lb $t1, s
lb $t2, p
# additione s + 1
add $t3, $t1, 1
#envoie la valeur contenue dans $t3 dans 0($t0)
sb $t3, 0($t0)
#additione s + p
add $t3, $t1, $t2
#envoie la valeur contenue dans $t3 dans 1($t0)
sb $t3, 1($t0)
# récupère 5($t0)
lb $t5, 5($t0)
# envoie la valeur de 5($t0) contenue dans $t5 dans 2($t2)
sb $t5, 2($t0)
li $v0, 10
syscall
