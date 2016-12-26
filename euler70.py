seznam = list(range(2, 10000000))
def euler_70(seznam):
    limit = len(seznam)
    i = 2
    stevec_indeksov = 0

    while i < limit:
        if seznam[stevec_indeksov] == i:
            for veckratnik in range(stevec_indeksov, limit, i):
                seznam[veckratnik] *= (1 - 1 / i)
                seznam[veckratnik] = int(seznam[veckratnik])
        i += 1
        stevec_indeksov += 1
    stevec = 2
    min_kvocient, resitev = (stevec / seznam[0]), 0
    for element in seznam:
        if sorted(str(element)) == sorted(str(stevec)):
            if (stevec / element) < min_kvocient:
                min_kvocient = (stevec / element)
                resitev = stevec
        stevec += 1
    return resitev