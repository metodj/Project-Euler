def primes(n):
    prastevila = []
    sieve = [True] * (n+1)
    for p in range(2, n+1):
        if (sieve[p]):
            prastevila.append(p)
        for i in range(p, n+1, p):
            sieve[i] = False
    return prastevila

praštevila = primes(1000)

def euler27():
    max_dolzina = 0
    for b in praštevila:
        for a in range(-1000, 1001):
            n = 1
            while is_prime(n * n + a * n + b):
                n += 1
                if n > max_dolzina:
                    max_dolzina, resitev = n, a * b

    return resitev, max_dolzina




from math import sqrt

def is_prime(n):
    if n <= 1: return False
    if n <= 3: return True
    if n%2==0 or n%3 == 0: return False
    r = int(sqrt(n))
    f = 5
    while f <= r:
        if n%f == 0 or n%(f+2) == 0: return False
        f+= 6
    return True

L = 1000
nmax = 0
for b in praštevila:
    for a in range(-b, b, 2):
        n = 1
        while is_prime(n*n + a*n + b): n += 1
        if n>nmax: nmax, p = n, a*b

print("Project Euler 27 Solution = ", p, "Sequence length =", nmax)


