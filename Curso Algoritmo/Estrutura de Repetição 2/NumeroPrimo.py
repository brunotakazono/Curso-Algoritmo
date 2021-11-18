count = 1
contDiv = 0
N = int(input('Digite um numero: '))

while True:
    if (N % count) == 0:
        contDiv = contDiv + 1
    count = count + 1
    if count > N:
        break

print('\n')
if contDiv > 2:
    print('O valor ', N, ' não é primo')
else:
    print('O valor ', N, ' é primo')


