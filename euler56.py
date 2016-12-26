def euler_56():
    vsota, max_sum = 0, 0
    for a in range(1, 101):
        for b in range(1, 101):
            for stevka in str(a ** b):
                vsota += int(stevka)
            if vsota > max_sum:
                max_sum = vsota
            vsota = 0
    return max_sum