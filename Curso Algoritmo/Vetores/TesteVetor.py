v = [1, 2, 3, 4, 5, 6]

for c in range(0, 6):
    v[c] = int(input("Digite o {0} valor: ".format(c)))

for c in range(0, 6):
    print('[', v[c], ']')
