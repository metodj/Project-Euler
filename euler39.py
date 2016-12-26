def euler39(n):
    max, stevilo_trikotnikov, resitev = 0, 0, 0
    for p in range(4, n, 2):
        for a in range(1, p//3 + 1):
            if (p * (p - 2 * a)) % (2 * (a - p)) == 0:
                stevilo_trikotnikov += 1
        if stevilo_trikotnikov > max:
            max = stevilo_trikotnikov
            resitev = p
        stevilo_trikotnikov = 0
    return resitev

print('Resitev je', euler39(1000))