def primes(n):
    prastevila = []
    sieve = [True] * (n+1)
    for p in range(2, n+1):
        if (sieve[p]):
            prastevila.append(p)
        for i in range(p, n+1, p):
            sieve[i] = False
    return prastevila

print(sum(primes(2000000)))

def je_prastevilo(n):
    s = 0
    for i in range(2, int(n**(1/2)) + 1):
        if n % i == 0:
            return False
    else:
        return True

def goldbach_test(n):
    s = 0
    m = 0
    k = 1
    niz = primes(n)
    if je_prastevilo(n):
        return True
    for i in range(0, len(niz)):
        while m < n:
            s += (int(niz[i]) + 2*(k**2))
            if s == n:
                return True
            m = s
            k += 1
            s = 0
        s = 0
        k = 1
        m = 0
    return False

def euler46(upper_limit):
    for i in range(3, upper_limit + 1, 2):
        if goldbach_test(i) == False:
            return i
    return 'Zvišaj mejo.'

