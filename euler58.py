def je_prastevilo(n):
    s = 0
    if n == 1:
        return False
    for i in range(2, int(n**(1/2)) + 1):
        if n % i == 0:
            return False
    else:
        return True

import time

def euler58():
    stevec, stevec_2, a, element, seznam = 0, 0, 2, 3, [1]
    while True:
        seznam.append(element)
        element += a
        stevec += 1
        if stevec == 4:
            element += 2
            a += 2
            stevec = 0
            for stevilo in seznam[len(seznam) - 4:]:
                if je_prastevilo(stevilo):
                    stevec_2 += 1
            if stevec_2 / len(seznam) < 0.1:
                return int((seznam[len(seznam) - 1])**(1/2))

print(time.clock(), euler58())