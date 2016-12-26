def euler21(n):
    vsota_deliteljev = 0
    druga_vsota = 0
    resitev = 0
    for i in range(1, n + 1):
        for k in range(1, i//2 + 1):
            if i % k == 0:
                vsota_deliteljev += k
        for r in range(1, vsota_deliteljev//2 + 1):
            if vsota_deliteljev % r == 0:
                druga_vsota += r
        if druga_vsota == i:
            resitev += i
        vsota_deliteljev = 0
        druga_vsota = 0
    return resitev
'''zgornji del kode je napisan napačno, za pravilno rešitev glej alternativno'''

def amicable(n):
    vsota_deliteljev = 0
    druga_vsota = 0
    for k in range(1, n//2 + 1):
        if n % k == 0:
            vsota_deliteljev += k
    for r in range(1, vsota_deliteljev//2 + 1):
        if vsota_deliteljev % r == 0:
            druga_vsota += r
    if (druga_vsota == n) and (n != vsota_deliteljev):
        return True
    else:
        return False

amicable(6)

def alternativno(n):
    s = 0
    for i in range (1, n+1):
        if amicable(i) == True:
            s += i
    return s

alternativno(100)






