ano_atual = int(input("Em que ano estamos? "))
ano_nasc = int(input("Em que ano eu nasci? "))

idade = ano_atual - ano_nasc

print('Em', ano_atual, 'voce tera', idade, 'anos')
if idade >= 21:
    print('E voce ja tera atingido maioridade')
else:
    print('Voce não atingiu a maioridade')
