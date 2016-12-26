def naslednji_clen(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1

def dolzina_zaporedja(n):
    if n == 1:
        return 1
    else:
        return 1 + dolzina_zaporedja(naslednji_clen(n))

def resitev(n):
    s = 0
    p = 0
    for i in range(1, n + 1,2):
        if dolzina_zaporedja(i) > p:
            s = i
            p = dolzina_zaporedja(i)
    return s

