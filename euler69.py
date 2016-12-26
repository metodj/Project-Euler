'''def GCD (m, n):
    if n == 0:
        return m
    else:
        return GCD(n, m % n)'''

'''from fractions import gcd'''

def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x

def euler69(n):
    max, resitev = 0.0, 0
    for stevilo in range(2, n + 1):
        sez = [prime_candidat for prime_candidat in range(1,stevilo) if gcd(stevilo, prime_candidat) == 1]
        if stevilo/len(sez) > max:
            max = stevilo/len(sez)
            resitev = stevilo
    return resitev

'''zgornja koda je pravilna, vendar je time inefficient'''

def je_prastevilo(n):
    s = 0
    for i in range(2, int(n**(1/2)) + 1):
        if n % i == 0:
            return False
    else:
        return True

def primes(n):
    return [i for i in range (1, n + 1) if je_prastevilo(i)]

def euler69_2(meja):
    niz_prastevil, resitev = primes(100), 1
    for x in niz_prastevil:
        resitev *= x
        if resitev > meja:
            return int(resitev / x)


