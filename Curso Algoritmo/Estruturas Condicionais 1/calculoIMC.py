M = float(input('Massa (Kg):'))
A = float(input('Altura (m):'))

IMC = M / (A ** 2)

print(IMC)

if (IMC >= 18.5) and (IMC < 25):
    print('Parabens! Voce esta no peso ideal')
else:
    print('Voce não esta na faixa de peso ideal')