list = open('base.txt.txt')

import math
seznam_stevil = []
for element in list:
    seznam_stevil.append((element[:len(element) - 1]))

def euler99():
    podseznam, max_1, max_2, resitev = [], 1, 1, 0
    for i in range(0, len(seznam_stevil)):
        podseznam = seznam_stevil[i].split(',')
        if (int(podseznam[1]) * math.log10(int(podseznam[0]))) > (max_2 * math.log10(max_1)):
            max_1 = int(podseznam[0])
            max_2 = int(podseznam[1])
            resitev = i
    return resitev + 1