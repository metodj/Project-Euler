koliko = 0
for stevilo in range(1, 1000001):
    if str(stevilo) == str(stevilo)[::-1]:
        if str(bin(stevilo))[2:] == str(bin(stevilo))[:1:-1]:
            koliko += stevilo

print(koliko)