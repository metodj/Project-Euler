def euler_119(n):
    vsota, i, seznam = 0, 1, []
    for stevilo in range(10, n + 1):
        for stevka in str(stevilo):
            vsota += int(stevka)
        if vsota == 1:
            vsota = 0
            continue
        while (vsota ** i) <= stevilo:
            if (vsota ** i) == stevilo:
                seznam.append(stevilo)
            i += 1
        i, vsota= 1, 0
    return seznam



def sum_of_digits(n):
  return sum(map(int, str(n)))

a = []
n = 30
for b in range(2, 100):
    for e in range(2, 10):
        p = b ** e
        if sum_of_digits(p) == b:
            a.append(p)

a.sort()
print("Answer to PE119 = a(%d) =" % n, a[n-1])