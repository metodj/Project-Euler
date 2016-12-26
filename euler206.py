def euler206():
    for kandidat in range(10 ** 9, 10 ** 10):
        test = str(kandidat ** 2)
        if len(test) == 19:
            if test[0] == '1':
                if test[2] == '2':
                    if test[4] == '3':
                        if test[6] == '4':
                            if test[8] == '5':
                                if test[10] == '6':
                                    if test[12] == '7':
                                        if test[14] == '8':
                                            if test[16] == '9':
                                                if test[18] == '0':
                                                    return kandidat




def ujemanje(n):
    niz = str(n)
    return all(int(niz[2*i]) == i + 1 for i in range(9))

def euler_206():
    n = 138902663  # sqrt(19293949596979899), niclo lahko izpustim, na koncu pomznozim n z 10
    while ujemanje(n * n) == False:
        n -= 2
    return n * 10