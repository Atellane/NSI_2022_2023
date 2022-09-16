li $t1, 4
li $t2, 3
li $t3, -3
add $t4, $t1, $t2
sub $t5, $t1, $t3
beq $t4, $t5, vrai
vrai:
li $v0, 1
li $a0, 1
syscall
li $v0, 10
syscall