def euler57():
    stevec, imenovalec, counter, koliko = 3, 2 , 0, 0
    while counter < 1000:
        stevec, imenovalec = 2 * imenovalec + stevec, stevec + imenovalec
        if len(str(stevec)) > len(str(imenovalec)):
            koliko += 1
        counter += 1
    return koliko