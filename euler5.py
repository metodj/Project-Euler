def euler5(n):
    s = 0
    for i in range (10000000, 1000000000, 20):
        for k in range (1,n+1):
            if i % k != 0:
                s += 1
        if s == 0:
            return i
        s = 0



