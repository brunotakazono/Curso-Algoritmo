import os

Mai = 0

def topo():
    os.system('CLS')
    print('-' * 30)
    print(" D E T E C T O R   DE   P E S A D O ")
    print(" Maior Peso ate agora: ", Mai, "Kg")
    print('-' * 30)



topo()

for i in range(1, 6):

    N = str(input("Digite o nome: "))
    P = int(input("Digite o peso de {0}: ".format(N)))
    if P > Mai:
        Mai = P
        Pesado = N
    topo()
