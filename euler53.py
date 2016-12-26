def fakulteta(n):
    resitev = 1
    for i in range(1, n + 1):
        resitev *= i
    return resitev

def n_nad_r(n, r):
    return int(fakulteta(n) / (fakulteta(r) * fakulteta(n - r)))


def koliko(n):
    stevec = 0
    for i in range(1, n + 1):
        for r in range(1, i):
            if n_nad_r(i, r) > 1000000:
                stevec += 1
    return stevec