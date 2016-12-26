
matrika = [vrstica.split() for vrstica in open('pathsum1.txt').readlines()]

for j in range(len(matrika)):
    for i in range(len(matrika[j])):
        matrika[j][i] = int(matrika[j][i])

for vrsta in range(len(matrika) - 1, 0, - 1):
    for stolpec in range(vrsta):
        matrika[vrsta - 1][stolpec] += max(matrika[vrsta][stolpec], matrika[vrsta][stolpec + 1])


print(matrika[0][0])