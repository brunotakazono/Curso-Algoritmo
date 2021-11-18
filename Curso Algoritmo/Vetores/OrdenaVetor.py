vet = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range(0, 10):
    vet[i] = int(input('Digite um valor :'))

for i in range(0, 9):
    for j in range(i+1, 10):
        if vet[i] > vet[j]:
            aux = vet[i]
            vet[i] = vet[j]
            vet[j] = aux

for i in range(0,10):
    print('[', vet[i], ']')