def test(n):
    niz = str(n)
    for i in range(2, 7):
        podniz = str(i*n)
        for znak in podniz:
            if znak not in niz:
                return False
    else:
        return True


def euler5200(n):
    niz = 'Zvisaj mejo.'
    s = 1
    while s < n:
        if test(s):
            return s
        s += 1
    return niz