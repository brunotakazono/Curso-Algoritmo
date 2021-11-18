soma = 0
div_5 = 0
nulo = 0
soma_pares = 0
for C in range(1, 6):
    valor = int(input(f'Digite o {C} o. Valor: '))
    soma = soma + valor
    if valor % 5 == 0:
        div_5 = div_5 + 1

    if valor == 0:
        nulos = nulos + 1
    if valor % 2 == 0:
        soma_pares = soma_pares + valor

media = soma / (C - 1)
print("A soma entre os valores e ", soma)
print('A media entre os valores {:.1f}'.format(media))
print("Valores divisiveis por cinco: ", div_5)
print("Valores nulos: ", nulo)
print("A soma dos valores pares e ", soma_pares)
