termo1 = 0
print(termo1)
termo2 = 1
print(termo2)


def rec_fib(n):
    if n > 1:
        return rec_fib(n - 1) + rec_fib(n - 2)
    return n


for i in range(3, 6):
    print(rec_fib(i))
