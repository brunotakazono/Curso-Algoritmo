print("------------------------")
print(" Escola Santa Paciencia ")
print("------------------------")
total_alunos = int(input('Quantos alunos a turma tem?'))
cont = 1
maiorNota = 0
while cont <= total_alunos:
    print("---------------")
    print("ALUNO ", cont)
    nome = str(input("Nome do aluno: "))
    nota = float(input("Nota de " + nome + ": "))
    if nota > maiorNota:
        maiorNota = nota
        melhorAluno = nome
    cont = cont + 1

print("-------------------")
print("O melhor aproveitamento foi de ", melhorAluno, " com a nota ", maiorNota)
