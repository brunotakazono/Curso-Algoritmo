import sys

R = 'S'
while True:
    N = int(input('Digite um número:'))
    C = N
    F = 1
    while True:
        F = F * C
        C = C - 1
        if C < 1:
            print('O Valor de fatorial de', N, 'é', F)
            R = str(input('Deseja Continuar [S/N]'))
            if R == 'S':
                break
            else:
                print('saindo do sistema até logo.')
                sys.exit()