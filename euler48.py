def euler48(n):
    s = 0
    for i in range(1, n + 1):
        s += i ** i
    s = str(s)
    return s[len(s)-10:len(s)]

def prastevila_do(n):
    s = 0
    prastevila = [2]
    for i in range(3, n + 1, 2):
        for k in range(1, int(i**(1/2)) + 1):
            if i % k == 0:
                s += 1
        if s <= 1:
            prastevila.append(i)
        s = 0
    return prastevila


# zelo hitrejša verzija
def primes(n):
    prastevila = []
    sieve = [True] * (n+1)
    for p in range(2, n+1):
        if (sieve[p]):
            prastevila.append(p)
        for i in range(p, n+1, p):
            sieve[i] = False
    return prastevila

# še hitrejša verzija s print
def primes_s_print(n):
  sieve = [True] * (n+1)
  for p in range(2, n+1):
    if (sieve[p]):
      print(p)
      for i in range(p, n+1, p):
        sieve[i] = False



