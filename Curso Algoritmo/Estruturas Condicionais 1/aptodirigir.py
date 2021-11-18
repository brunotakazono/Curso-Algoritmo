print('-------------------------')
print('DEPARTAMENTO DE TRANSITO')
print('-------------------------')




ano_atual = int(input("Ano Atual (YYYY): "))
ano_nasc =  int(input("Ano Nascimento (YYYY): "))

idade = ano_atual - ano_nasc

print('-------STATUS---------')
print('----------------------')

print('IDADE:', idade, 'ANOS')
if idade >=18:
    print('APTO A TIRAR A CARTEIRA')
else:
    print('INAPTO A TIRAR A CARTEIRA')

