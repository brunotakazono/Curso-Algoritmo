T1 = 0
print(T1, '', end='')
T2 = 1
print(T2, '', end='')
for c in range(3, 16):
    T3 = T1 + T2
    print(T3, '', end='')
    T1 = T2
    T2 = T3