def monnaie_rendue():
    sys_monnaie_euro = (500, 200, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01) 
    a_rendre = 2.63 
    return glouton(sys_monnaie_euro, a_rendre) 

 

def glouton(sys_monnaie_euro, a_rendre): 
    solution = []
    a_rendre *= 100
    for i in range (len(sys_monnaie_euro)): 
        while a_rendre >= sys_monnaie_euro[i] * 100: 
            a_rendre -= sys_monnaie_euro[i] * 100
            solution.append(sys_monnaie_euro[i]) 
    return solution

solution: list = monnaie_rendue()

print(f"Le programme pour rendre 2.63 € a utilisé {len(solution)} pièces qui sont :")
for i in solution:
    print(i)