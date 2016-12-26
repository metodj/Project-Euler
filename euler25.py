def fib(n):
    fibs = [1, 1]
    for i in range(2, n+1):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs[n-1]

def euler25(n):
    i = 1
    niz = ''
    while True:
        niz += str(fib(i))
        if len(niz) > (n - 1):
            return i
        niz = ''
        i += 1

