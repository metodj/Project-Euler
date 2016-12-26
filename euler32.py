def euler38():
    kandidat, niz, seznam, s, t= '', '123456789', [], 0, 1
    for clen_1 in range(1, 500):
        for clen_2 in range(1, 5000):
            kandidat = str(clen_1) + str(clen_2) + str(clen_1 * clen_2)
            if len(kandidat) != 9:
                continue
            for stevka in niz:
                if stevka not in kandidat:
                    break
                else:
                    s += 1
            if s == 9:
                for i in range(0, len(seznam)):
                    if (clen_1 * clen_2) == seznam[i]:
                        t = 0
                        break
                if t == 1:
                    seznam.append(clen_1 * clen_2)
            s = 0
            t = 1
    return sum(seznam)



print('Vsota znasa:', euler38())