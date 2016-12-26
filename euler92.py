def test89(stevilo):
    nova_stevka = 0
    while stevilo:
        nova_stevka += (stevilo % 10) ** 2
        stevilo //= 10
    if (nova_stevka == 89) or (nova_stevka == 145):
        return True
    elif (nova_stevka == 1) or (nova_stevka == 44):
        return False
    else:
        return test89(nova_stevka)



def euler92():
    koliko = 0
    for stevilo in range(1, 10000001):
        if test89(stevilo):
            koliko += 1
    return koliko