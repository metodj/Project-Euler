def faktorizacija(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)
            n //= d
        d += 1
    if n > 1:
       primfac.append(n)
    return set(primfac)


def euler47(n):
    stevec = 0
    for stevilo in range(1, n):
        for k in range(0, 4):
            if len(faktorizacija(stevilo + k)) != 4:
                break
            else:
                stevec += 1
        if stevec == 4:
            return stevilo
        stevec = 0
    return 'Zvisaj mejo!'