def euler9():
    for a in range(3, 500):
        for b in range(a, 500):
            if ((a ** 2 + b ** 2) ** (1/2)).is_integer():
                if a + b + ((a ** 2 + b ** 2) ** (1/2)) == 1000:
                    return int(a * b * ((a ** 2 + b ** 2) ** (1/2)))

print(euler9())