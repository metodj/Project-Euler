def palindrom(niz):
    return niz == niz[::-1]

def euler4(n):
    kandidat = ''
    resitev = []
    for i in range(100, n):
        for k in range(100, n):
            kandidat = str(i*k)
            if palindrom(kandidat) == True:
                kandidat = int(kandidat)
                resitev.append(kandidat)
            kandidat = ''
    return max(resitev)


