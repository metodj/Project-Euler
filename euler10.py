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