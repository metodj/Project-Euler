def primes(n):
    prastevila = []
    sieve = [True] * (n+1)
    for p in range(2, n+1):
        if (sieve[p]):
            prastevila.append(p)
        for i in range(p, n+1, p):
            sieve[i] = False
    return prastevila

def je_prastevilo(n):
    s = 0
    for i in range(2, int(n**(1/2)) + 1):
        if n % i == 0:
            return False
    else:
        return True

def euler50(n):
    niz = primes(n)
    vsota = 0
    max_dolzina = 0
    resitev = 0
    counter = 0
    for zacetni in range(0, len(niz) - 1):
        while vsota < n:
            vsota += niz[zacetni]
            zacetni += 1
            counter += 1
            if je_prastevilo(vsota) and (vsota < n) :
                if counter > max_dolzina:
                    max_dolzina = counter
                    resitev = vsota
        vsota = 0
        counter = 0
    return resitev









