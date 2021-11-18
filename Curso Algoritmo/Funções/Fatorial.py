def Fatorial(V):
    r = 1
    for num in range(1, V + 1):
        r *= num
    return r


N = int(input('Digite um numero:'))
F = Fatorial(N)

print('O valor de ', N, '! é igual a', F)
