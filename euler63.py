def euler63_alternativno():
    koliko = 0
    for stevilo in range(2, 10):
        for eksponent in range(1, 100):
            if eksponent == len(str(stevilo ** eksponent)):
                koliko += 1
    return koliko + 1 #prištejem še enko (1 ** 1)