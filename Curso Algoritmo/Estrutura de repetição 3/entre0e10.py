Tot010 = 0
SImp = 0
for c in range(1, 7):
    V = int(input('Digite um valor: '))
    if 0 <= V <= 10:
        Tot010 = Tot010 + 1
    if V % 2 == 1:
        SImp = SImp + V

print('Ao todo foram', Tot010, ' valores entre 0 e 10')
print('Nesse intervalo, a soma de impares foi ', SImp)
