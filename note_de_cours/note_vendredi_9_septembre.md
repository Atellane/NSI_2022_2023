# cours vendredi 9 septembre
site visité pdt le cours :<br />
[simulation gestion unité logique processeur](http://www.balance3e.com/source.html)<br />
assembleur:<br />
instruction pour `9-2`:<br />
```mips
		LOADC #9
		STORE 0
		LOADC #2
		STORE 1
		LOADA 0
		LOADB 1
		SUB
		STORE 0
```
instruction pour `5*12`:
```mips
		LOADC #5
		STORE 0
		LOADC #5
		STORE 1
		LOADC #1
		STORE 2
		LOADC #1
		STORE 3
		LOADA 0
		LOADB 1
		ADD
		STORE 0
		LOADA 2
		LOADB 3
		ADD
		STORE 2
		LOADA #12
		LOADB 2
		EQUAL
		JUMP 9
		HALT
```