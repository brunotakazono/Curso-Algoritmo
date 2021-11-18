time=  [1, 2, 3]

print("------------------")
print("CAMPEONATO FUTEBOL")
print("------------------")

for c in range(0, 3):
    time[c] = str(input(f"Nome do {c} time: "))

print("-------------------")
print(" TABELA DE PARTIDAS")
print("-------------------")

for l in range(0, 3):
    for c in range(0, 3):
        if l != c:
            print(time[l] , " [ ] x [ ] ", time[c])