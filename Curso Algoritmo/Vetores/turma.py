nome = [1, 2, 3, 4]
n1 = [1, 2, 3, 4]
n2 = [1, 2, 3, 4]
m = [1, 2, 3, 4]
SM = 0
Tot = 0

for i in range(0, 4):
    print('Aluno', i)
    nome[i] = str(input('Nome: '))
    n1[i] = float(input('Primeira Nota:'))
    n2[i] = float(input('Segunda Nota:'))
    m[i] = (n1[i] + n2[i]) / 2
    SM = SM + m[i]
MT = SM / 4
print(' LISTAGEM DE ALUNOS')
print('---------------------------')

for i in range(0, 4):
    print(nome[i], m[i], )
    if m[i] > MT:
        Tot = Tot + 1

print('Ao todos temos', Tot, 'alunos acima da médiada turma que é', MT)
