def euler30(n):
    s = 0
    resitev = 0
    for i in range(2, n + 1):
        niz = str(i)
        for stevka in niz:
            s += int(stevka)**5
            if s > i:
                continue
        if s == i:
            resitev += i
        s = 0
    return resitev