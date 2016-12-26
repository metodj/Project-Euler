def euler31():
    stevilo_moznosti = 1
    #moznost z enim po 200 privzamemo ze kar na zacetku
    kovanci = [1, 2, 5, 10, 20, 50, 100]
    for a in range(0, 201):
        for b in range(0, 101):
            if a * 1 + b * 2 > 200:
                break
            else:
                for c in range(0, 41):
                    if a * 1 + b * 2 + c * 5 > 200:
                        break
                    else:
                        for d in range(0, 21):
                            if a * 1 + b * 2 + c * 5 + d * 10 > 200:
                                break
                            else:
                                for e in range(0, 11):
                                    if a * 1 + b * 2 + c * 5 + d * 10 + e * 20 > 200:
                                        break
                                    else:
                                        for f in range(0, 5):
                                            if a * 1 + b * 2 + c * 5 + d * 10 + e * 20 + f * 50 > 200:
                                                break
                                            else:
                                                for g in range(0, 3):
                                                    if a * 1 + b * 2 + c * 5 + d * 10 + e * 20 + f * 50 + g * 100 == 200:
                                                       stevilo_moznosti += 1
                                                    elif a * 1 + b * 2 + c * 5 + d * 10 + e * 20 + f * 50 + g * 100 > 200:
                                                        break
    return stevilo_moznosti