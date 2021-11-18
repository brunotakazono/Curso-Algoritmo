S = 0
resp = 'S'
while resp == 'S':
    N = int(input('Digite um valor ==>'))
    S = S + N
    resp = str(input('Voce quer continuar ? [S/N]'))
print('A soma de todos os valores digitados é', S)

