M = float(input('Massa (Kg):'))
A = float(input('Altura (m):'))

IMC = M / (A ** 2)

print(IMC)

if IMC < 17:
    print('Muito abaixo do peso')

else:
    if (IMC >= 17) and (IMC <= 18.5):
        print('Abaixo do peso')
    else:
        if (IMC >= 18.5) and (IMC < 25):
            print('Parabens! Voce esta no peso ideal')
        else:
            if (IMC >= 25) and (IMC < 30):
                print('Sobrepeso')
            else:
                if (IMC >= 30) and (IMC < 35):
                    print('Obesidade')
                else:
                    if  (IMC >= 35) and (IMC < 40):
                        print('Obesidade Severa')
                    else:
                        print('Obesidade Mórbida')