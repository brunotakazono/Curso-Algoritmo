valor_emprestimo = float(input('Qual o valor do emprestimo? '))
quantidade_parcelas = int(input('Quantas Parcelas? '))
juros = valor_emprestimo*(20/100)
vou_pagar = (valor_emprestimo+juros)/quantidade_parcelas
valor_total = valor_emprestimo+juros


print('valor total do emprestimo acrescido de juros {:.2f}'.format(valor_total))
print('Vou Pagar', quantidade_parcelas, 'parcelas de {:.2f}'.format(vou_pagar))