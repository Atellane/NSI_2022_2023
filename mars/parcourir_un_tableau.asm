.data
tab: .byte 1, 2, 3, 4
break_line: .asciiz "\n"
.text
la $t1, tab
# 0($t1) = première adresse du tableau, 1($t1) = deuxième adresse du tableau, etc
lb $t2, 0($t1)
li $v0, 1
move $a0, $t2
syscall
addi $v0, $zero, 4
la $a0, break_line 
syscall
lb $t2, 1($t1)
li $v0, 1
move $a0, $t2
syscall
addi $v0, $zero, 4
la $a0, break_line
syscall
lb $t2, 2($t1)
li $v0, 1
move $a0, $t2
syscall
addi $v0, $zero, 4
la $a0, break_line 
syscall
lb $t2, 3($t1)
li $v0, 1
move $a0, $t2
syscall
li $v0, 10
syscall