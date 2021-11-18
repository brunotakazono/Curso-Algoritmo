import sys

while True:
    print('')
    print("=================")
    print("|    M E N U    |")
    print("=================")
    print("| [1] De 1 a 10 |")
    print("| [2] De 10 a 1 |")
    print("| [3] Sair      |")
    print("=================")
    op = int(input('Escolha uma opção: '))
    if op == 1:
        cont = 1
        while True:
            print(cont, ' ', end='')
            cont = cont + 1
            if cont > 10:
                break
    elif op == 2:
        cont = 10
        while True:
            print(cont, ' ', end='')
            cont = cont - 1
            if cont < 1:
                break
    else:
        print('saindo do sistema até logo.')
        sys.exit()