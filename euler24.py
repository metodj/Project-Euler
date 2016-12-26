from itertools import permutations

#niz = '0123456789'
#print(sorted([ int(''.join(permutacija)) for permutacija in permutations(niz)]))


def euler24():
    niz = '0123456789'
    m = sorted([ int(''.join(permutacija)) for permutacija in permutations(niz)])
    return m[1000000 - 1]

print([euler24()])