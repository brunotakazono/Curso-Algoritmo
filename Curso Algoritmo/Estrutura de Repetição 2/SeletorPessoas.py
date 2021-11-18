TotH18 = 0
TotM25 = 0

while True:
    print('==========================')
    print('    SELETOR DE PESSOAS    ')
    print("==========================")
    sexo = str(input('Qual o Sexo? [M/F] :'))
    idade = int(input('Qual a idade? : '))
    print('---------------------')
    print('[1] Preto')
    print('[2] Castanho')
    print('[3] Loiro')
    print('[4] Ruivo')
    cabelo = int(input('Qual a cor do Cabelo?:'))
    if sexo == "M" and idade > 18 and cabelo == 2:
        TotH18 = TotH18 + 1
    elif sexo == "F" and 25 <= idade <= 30 and cabelo == 3:
        TotM25 = TotM25 + 1
    resp = str(input('Deseja Continuar [S/N]'))
    if resp == 'S':
        continue
    else:
        break

print('------------------------------------')
print(' RESULTADO FINAL ')
print('------------------------------------')
print('Total de homens com mais de 18 e cabelos castanhos ', TotH18)
print('Total de mulheres entre 25 e 30 e cabelos loiros ', TotM25)
