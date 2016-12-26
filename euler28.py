def euler28(n):
    vsota, i, stevec, m = 1, 3, 0, 2
    while i <= n:
        vsota += i
        i += m
        stevec += 1
        if stevec == 4:
            i += 2
            m += 2
            stevec = 0
    return vsota

def pomozna():
    i = 1
    while euler28(i) != 101:
        i+= 1
    return i