from fractions import Fraction

def euler33():
    stevec, resitev = 0, []
    for stevilo in range(11, 100):
        if stevilo % 10 == 0:
            continue
        for stevilo_2 in range(stevilo + 1, 100):
            for stevka in str(stevilo):
                if stevka in str(stevilo_2):
                    novo= str(stevilo).replace(stevka,'')
                    novo_2 = str(stevilo_2).replace(stevka, '')
                    if novo != '' and novo_2 != '' and novo_2 != '0':
                        if (int(novo) / int(novo_2)) == (stevilo / stevilo_2):
                            resitev.append(Fraction(stevilo, stevilo_2))
                    break
    return resitev



print(euler33())