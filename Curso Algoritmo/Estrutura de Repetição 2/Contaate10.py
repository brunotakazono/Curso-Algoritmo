contador = 1
N = int(input('Quer ver a tabuada de qual numero: '))

while True:
    R = N * contador
    print(N, 'x',contador, '=', R)
    contador = contador + 1
    if (contador > 10):
        break
