import os
B = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]


def MostraFileira():

    for i in range(0, 10):
        if B[i] == '':
            print(f'[B {[i]} ]')
        else:
            print("[ --- ]")
    print()
    print("------------------------------------------------------------------------")


while True:
    os.system('CLS')
    MostraFileira()
    cad = int(input("Reservar a cadeira: B"))
    if B[cad] == "":
        B[cad] = "X"
        print("Cadeira B", cad, " RESERVADA!")
    else:
        print("ERRO: Lugar Ocupado!")

    r = str(input("Quer reservar outro? [S/N] "))
    if r == "N":
        break