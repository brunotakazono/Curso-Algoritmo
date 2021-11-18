val = [1, 2, 3, 4, 5, 6, 7]
TotPar=0

for i in range(0, 7):
    val[i] = int(input("Digite o {0} valor: ".format(i)))
    if val[i] % 2 == 0:
        TotPar = TotPar + 1

for i in range(0, 7):
    if val[i] % 2 == 0:
        print('Valor par na Posição', i)

print('O total de pares foi: ', TotPar)