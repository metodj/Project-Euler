
def particija_rekurzija(n, r):
    if r == 1:
        return 1
    elif r == n:
        return 1
    elif n < r:
        return 0
    else:
        return particija_rekurzija(n - 1, r - 1) + particija_rekurzija(n - r, r)


def euler76():
    koliko = 0
    for r in range (2, 101):
        koliko += particija_rekurzija(100, r)
    return koliko