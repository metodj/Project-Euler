def mavrica():
    list, stevec = [], 0
    barve = ['rdeca', 'oranzna', 'rumena', 'zelena', 'modra','svetlomodra', 'vijolicna' ]
    for element in barve:
        while stevec < 10:
            list.append(element)
            stevec += 1
        stevec = 0
    return list

import random

def posamezni_izbor(limit):
    kroglice, stevec, koliko= mavrica(), 0, []
    while stevec < limit:
        koliko.append(len(set(random.sample(kroglice, 20))))
        stevec += 1
    return round(sum(koliko) / len(koliko), 9)