def število_deliteljev(n):
    s = 1
    for i in range(1, n//2+1):
        if n % i == 0:
            s += 1
    return s

def n_ti_člen(n):
    return int(n*(n+1)/2)

def euler12():
    s = 0
    for i in range (1, 100000):
        s += i
        if število_deliteljev(s) == 500:
            return s
    return 'zvišaj mejo'


import math
from time import time
t = time()
def divisors(n):
    number_of_factors = 0
    for i in range(1, int(math.ceil(math.sqrt(n)))+1):
        if n % i == 0:
            number_of_factors +=2
        if i*i==n:
            number_of_factors -=1
    return number_of_factors

x=1
for y in range(2,1000000):
    x += y
    if divisors(x) >= 500:
        print (x)
        break
tt = time()-t
print (tt)

