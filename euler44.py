def euler44(n):
    pentagonal = set(int(i * (3 * i - 1) / 2) for i in range(1, n + 1))
    for i in pentagonal:
        for j in pentagonal:
            if (j + i) in pentagonal and (j - i) in pentagonal:
                return abs(j - i)
            else:
                continue
    return 'Zvisaj mejo!'