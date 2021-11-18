L1 = float(input('Digite o primeiro lado: '))
L2 = float(input('Digite o segundo lado: '))
L3 = float(input('Digite o terceiro lado: '))

TRI = (L1 < (L2+L3) and L2 < (L1 + L3) and L3 < (L1 + L2))
EQ = (L1 == L2 and L2 == L3)
ES = (L1 != L2 and L2 != L3 and L1 != L3 )

print('Pode formar um triângulo', TRI)
print('o triângulo é equilátero?', EQ)
print('o triângulo é escaleno?', ES)


