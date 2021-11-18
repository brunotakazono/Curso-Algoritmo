contador = 1
S = 0
maior = 0

while (contador <= 10):
    N = int(input('Digite um valor:'))
    print(N)
    if (N > maior):
        maior = N
    S = S + N
    contador += 1
print('A soma de todos os valores foi', S)
print('O maior valor digitado foi', maior)
