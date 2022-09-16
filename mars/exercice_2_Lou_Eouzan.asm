#les adresses des variables sont indiquées avec les commentaires qui les précède
.data
#0x10010000
o1: .byte, 1
#0x10010001
o2: .byte, 2
#0x10010002
o3: .byte, 3
#0x10010003
o4: .byte, 4
#0x10010004
m1: .word, 0xAABBCCDD
.text
la $t1, o1
la $t2, o2
la $t3, o3
la $t4, o4
la $t5, m1
li $v0, 10
syscall