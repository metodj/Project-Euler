matrika_moja = [list(map(int, element.split())) for element in (line.rstrip('\n') for line in open('20x20.txt'))]

def euler11():
    max_product = 0
    vrstice, stolpci = len(matrika_moja), len(matrika_moja[0])
    for i in range(vrstice):
        for j in range(stolpci - 3):
            produkt = matrika_moja[i][j] * matrika_moja[i][j + 1] * matrika_moja[i][j + 2] * matrika_moja[i][j + 3]
            if produkt > max_product:
                max_product = produkt
    for j in range(stolpci):
        for i in range(vrstice - 3):
            produkt = matrika_moja[i + 1][j] * matrika_moja[i + 2][j] * matrika_moja[i][j] * matrika_moja[i + 3][j]
            if produkt > max_product:
                max_product = produkt
    for j in range(stolpci - 3):
        for i in range(vrstice - 3):
            produkt = matrika_moja[i][j] * matrika_moja[i + 1][j + 1] * matrika_moja[i + 2][j + 2] * matrika_moja[i + 3][j + 3]
            if produkt > max_product:
                max_product = produkt
    for j in range(stolpci - 3):
        for i in reversed(range(3, vrstice)):
            produkt = matrika_moja[i][j] * matrika_moja[i - 1][j + 1] * matrika_moja[i - 2][j + 2] * matrika_moja[i - 3][j + 3]
            if produkt > max_product:
                max_product = produkt
    return max_product








