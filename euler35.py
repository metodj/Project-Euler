def je_prastevilo(n):
    s = 0
    for i in range(2, int(n**(1/2)) + 1):
        if n % i == 0:
            return False
    else:
        return True

def primes(n):
    prastevila = []
    sieve = [True] * (n+1)
    for p in range(2, n+1):
        if (sieve[p]):
            prastevila.append(p)
        for i in range(p, n+1, p):
            sieve[i] = False
    return prastevila

def euler35(seznam):
    resitev, t, m = 0, 1, 0
    for prastevilo in seznam:
        m = str(prastevilo)
        for i in range(1, len(m)):
            if not je_prastevilo(int(m[i:] + m[:i])):
                t = 0
                break
        if t == 1:
            resitev += 1
        t = 1
    return resitev