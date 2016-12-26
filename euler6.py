def euler6(n):
    s = 0
    t = 0
    for i in range(1,n+1):
        s += i**2
        t += i
    return t**2 - s
