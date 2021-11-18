'''valor = int(input('Digite um valor: '))

for cont in range(0, valor, 2):
    print(cont)'''



valor = int(input('Digite um valor: '))
if valor % 2 == 1:
     valor = valor - 1
for cont in range(valor, 0, -2):
    print(cont)
