#d(n) > n

import math

def d(n):
    s = 1
    t = math.sqrt(n)
    for i in range(2, int(t)+1):
        if n % i == 0: s += i + n/i
    if t == int(t): s -= t    #correct s if t is a perfect square
    return s

def abundant_test(n):
    if d(n) > n:
        return True
    return False




seznam_abundant = [k for k in range(1, 28123 + 1) if abundant_test(k)]

def je_abundant_vsota(n, seznam_abundant):
   for i in seznam_abundant:
       if i > n:
         return False
       for element in seznam_abundant:
           if element == (n - i):
               return True
           elif element > (n - i):
               break
   return False

def euler23(seznam):
    return sum(stevilo for stevilo in range(1, 28123 + 1) if not je_abundant_vsota(stevilo, seznam))



def euler23_alternativno():
    zgornja_meja, vsota = 28123, 0
    abnundant = set()
    for n in range(1, zgornja_meja):
        if d(n) > n:
            abnundant.add(n)
        if not any( (n-a in abnundant) for a in abnundant ):
            vsota += n
    return vsota














