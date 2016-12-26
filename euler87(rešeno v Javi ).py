def primes(n):
    prastevila = []
    sieve = [True] * (n+1)
    for p in range(2, n+1):
        if (sieve[p]):
            prastevila.append(p)
        for i in range(p, n+1, p):
            sieve[i] = False
    return prastevila

def test(n):
    niz = primes(150)
    for i in range(0, len(niz)):
        for k in range(0, len(niz) - i):
            for l in range(0, len(niz) - i):
                for j in range(0, len(niz) - i):
                    if (niz[i + k]**2 + niz[i + l]**3 + niz[i + j]**4) == n:
                        return True
    else:
        return False

def euler87_alternativno(n):
    koliko = 0
    niz = primes(84)
    for i in range(0, len(niz)):
        for k in range(0, len(niz) - i):
            for l in range(0, len(niz) - i):
                for j in range(0, len(niz) - i):
                    if (niz[i + k]**2 + niz[i + l]**3 + niz[i + j]**4) < n:
                        koliko += 1
    return koliko

def test_alternativno(n):
    i = 0
    niz = primes(150)
    kandidat = 0
    while kandidat < n:
        kandidat = niz[i]**2 + niz[i]**3 + niz[i]**4
        if kandidat == n:
            return True
        i += 1
    return False


def euler87(n):
    s = 0
    for i in range(1, n + 1):
        if test(i):
            s += 1
    return s




