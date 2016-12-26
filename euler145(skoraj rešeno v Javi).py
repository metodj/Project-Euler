def reverse(n):
    m = str(n)
    return m[::-1]

def test(n):
    m = reverse(n)
    if m[0] == '0':
        return False
    sum = str(n + int(m))
    for i in range(0, len(sum)):
        if (int(sum[i])% 2 == 0):
            return False
    else:
        return True

def euler145(n):
    koliko = 0
    for i in range(1, n + 1):
        if test(i):
            koliko += 1
    return koliko






