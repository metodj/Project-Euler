from itertools import permutations



def euler43():
    permutacije = []
    niz = []
    s = 0
    for i in range(0, 10):
        niz += str(i)
    for p in permutations(niz):
        if p[0] != str(0):
            permutacije.append(''.join(p))
    for k in range(0, len(permutacije)):
        kandidat = permutacije[k]
        if int(kandidat[7:10]) % 17 == 0:
            if int(kandidat[6:9]) % 13 == 0:
                if int(kandidat[5:8]) % 11 == 0:
                    if int(kandidat[4:7]) % 7 == 0:
                        if int(kandidat[3:6]) % 5 == 0:
                            if int(kandidat[2:5]) % 3 == 0:
                                if int(kandidat[1:4]) % 2 == 0:
                                    s +=int(kandidat)
    return s
























