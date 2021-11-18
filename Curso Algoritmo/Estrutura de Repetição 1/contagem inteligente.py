contador = 0

print('CONTAGEM INTELIGENTE')
print('--------------------')
inicio = int(input('Inicio : '))
fim = int(input('Fim :'))
print("--------------------")
print("  C O N T A N D O   ")
print("--------------------")
if fim > inicio:
    contador = inicio
    while contador <= fim:
        print (contador, '..', end='')
        contador = contador + 1
else:
    contador = inicio
    while contador >= fim :
        print (contador, '..', end='')
        contador = contador - 1