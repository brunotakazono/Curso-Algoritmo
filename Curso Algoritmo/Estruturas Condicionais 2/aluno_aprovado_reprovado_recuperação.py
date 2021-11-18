N1 = float(input('Primeira Nota: '))
N2 = float(input('Segunda Nota: '))

M = (N1+N2)/2

print('-----------------------')
print('A média do aluno foi: {:.2f}'.format(M))
if M >= 7:
    print('ALUNO APROVADO')
else:
    if (M >= 5)  and (M < 7):
        print('ALUNO EM RECUPERAÇÃO')
    else:
        print('ALUNO REPROVADO')
print('-----------------------')

