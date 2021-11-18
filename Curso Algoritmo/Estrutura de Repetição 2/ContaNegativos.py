total_negativos = 0
c=1
while True:
    N = int(input('Digite um numero :'))
    if N < 0:
        total_negativos = total_negativos + 1
    c = c + 1
    if c > 5:
        break
print('O total de numeros negativos é ', total_negativos)