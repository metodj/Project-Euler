def triangle(n):
    seznam = []
    for i in range(286, n + 1):
        seznam.append(i * ( i + 1 ) // 2)
    return seznam

def pentagonal(n):
    seznam = []
    for i in range(166, n + 1):
        seznam.append(i * ( 3 * i - 1 ) // 2)
    return seznam

def hexagonal(n):
    seznam = []
    for i in range(144, n + 1):
        seznam.append(i * ( 2 * i - 1 ))
    return seznam


def euler45(n):
    niz_1, niz_2, niz_3 = triangle(n), pentagonal(n), hexagonal(n)
    for i in range(0, len(niz_1)):
        for k in range(0, len(niz_2)):
            if niz_2[k] > niz_1[i]:
                break
            elif niz_2[k] != niz_1[i]:
                continue
            else:
                for l in range(0, len(niz_3)):
                    if niz_3[l] > niz_2[k]:
                        break
                    elif niz_3[l] != niz_2[k]:
                        continue
                    else:
                        return niz_1[i]
    return 'Zvisaj mejo!'

def hexagonal(n):
    return [int(n * (2 * n - 1))  for n in range(143, n + 1)]

def pentagonal(n):
    return [int(n * (3 * n - 1) / 2) for n in range(165, n + 1)]

def euler45_alternativno(pen, hex):
    indeks_p, indeks_h = 0, 0
    p = pen[indeks_p]
    h = hex[indeks_h]
    while True:
        while p < h:
            indeks_p += 1
            p = pen[indeks_p]
        if h == p and (h != 40755):
            return p
        indeks_h += 1
        h = hex[indeks_h]
    return 'zvisaj mejo'




