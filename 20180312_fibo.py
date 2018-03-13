def fibo(n):
    if n==1 or n==2:
        return 1

    else:
        return fibo(n-1)+fibo(n-2)

print(fibo(8))


def fibo(n1, n2):
    if n1 > 100:
        return
    n3 = n1 + n2
    print(n2)
    fibo(n2, n3)

fibo(0, 1)



from functools import reduce
print(reduce(lambda fib, c: fib.append((fib[-2] + fib[-1])) or fib, range(20), [1, 1]))

L = [1, 1]
for i in range(10):
    L.append(L[-2] + L[-1])
print(L)

L = [1, 1]
for i in range(10):
    L.append(sum(L[i:]))
print(L)
