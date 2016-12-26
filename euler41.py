from itertools import permutations

def permutacije(n):
    niz = []
    resitev = []
    for i in range(1, n + 1):
        niz += str(i)
    for stevilo in permutations(niz):
        resitev.append(''.join(stevilo))
    return resitev

def je_prastevilo(n):
    for i in range(2,int(n**(1/2)) + 1):
        if n % i == 0:
            return False
    return True

def euler41():
    max_prastevilo = 0
    for i in range(5, 10):
        m = permutacije(i)
        for stevilo in range(0, len(m)):
            if je_prastevilo(int(m[stevilo])):
                if int(m[stevilo]) > max_prastevilo:
                    max_prastevilo = int(m[stevilo])
    return max_prastevilo
