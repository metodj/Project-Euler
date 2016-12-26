def je_1do9_pandigital(stevilo):
    test = '123456789'
    for znak in test:
        if znak not in stevilo:
            return False
    return True

def euler38(n):
    m, niz, max_pandigital = 1, '', 1
    for stevilo in range(1, n + 1):
        while len(niz) < 9:
            niz += str(m * stevilo)
            m += 1
        if len(niz) == 9:
            if je_1do9_pandigital(niz):
                if int(niz) > max_pandigital:
                    max_pandigital = int(niz)
        niz = ''
        m = 1
    return max_pandigital