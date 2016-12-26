def euler62():
    n, digits, slovar = 100, '', {}
    while True:
        kub = n ** 3
        digits = ''.join(sorted(str(kub)))
        if digits in slovar:
            slovar[digits] += [kub]
            if len(slovar[digits]) == 5:
                return slovar[digits][0]
        else:
            slovar[digits] = [kub]
        n += 1