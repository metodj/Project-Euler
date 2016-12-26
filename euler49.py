def prastevilo(n):
    for i in range(2, int(n**(1/2)) + 1):
        if n % i == 0:
            return False
    return True



def vaja(n):
    resitev = []
    m = 0
    for i in range(1000, n + 1, 2):
        niz = str(i)
        niz_3330 = str(i + 3330)
        niz_6660 = str(i + 6660)
        for znak in niz:
            if znak in niz_3330:
                if znak in niz_6660:
                    if prastevilo(int(niz_3330)):
                        if prastevilo(int(niz_6660)):
                            if prastevilo(int(niz)):
                                m += 1
        if m == 4:
            resitev.append(niz + niz_3330 + niz_6660)
        m = 0
    return resitev











