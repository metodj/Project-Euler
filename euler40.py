import time

def champer(n):
    niz, resitev, s = '', 1, 1
    for i in range(1, n):
        niz += str(i)
    while s <= n:
        resitev *= int(niz[s -1])
        s *= 10
    return resitev


print(champer(1000000))