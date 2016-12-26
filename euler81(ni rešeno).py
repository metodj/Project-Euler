
matrika = [vrstica.split(',') for vrstica in open('matrix_80x80.txt')]

def euler81():
    i, j, vsota = 79, 79, 0
    while i != 0 and j != 0:
        vsota += int(matrika[i][j])
        if j == 0:
            i -= 1
        elif i == 0:
            j -= 1
        else:
            if matrika[i][j - 1] < matrika[i - 1][j]:
                j -= 1
            else:
                i -= 1
    return vsota
