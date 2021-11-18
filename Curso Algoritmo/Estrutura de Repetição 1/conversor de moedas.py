c = 1

Q = int(input('Quantas vezes você deseja realizar a conversão? '))
while c <= Q:

    R = float(input('Qual o valor em R$?'))
    print(R)
    D = R/2.20
    print('O valor convertido é US$ {:.2f}'.format(D))
    c = c + 1
