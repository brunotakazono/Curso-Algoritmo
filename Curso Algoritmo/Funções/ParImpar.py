def ParOuImpar(V):
    if V % 2 == 0:
        return 'PAR'
    else:
        return 'IMPAR'





N = int(input('Digite um numero:'))
R = ParOuImpar(N)

print('O valor', N, 'é um valor', R)