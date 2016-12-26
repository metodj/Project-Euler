def increasing(n):
    prejsnja_stevka = 0
    for stevka in str(n):
        if not int(stevka) >= prejsnja_stevka:
            return False
        prejsnja_stevka = int(stevka)
    return True




def decreasing(n):
    prejsnja_stevka = float('inf')
    for stevka in str(n):
        if not int(stevka) <= prejsnja_stevka:
            return False
        prejsnja_stevka = int(stevka)
    return True

def bouncy(n):
    if decreasing(n) or increasing(n):
        return False
    return True



def euler112(iskani_kvocient):
    koliko, kvocient, stevilo =0, 0, 99
    while kvocient < iskani_kvocient:
        if bouncy(stevilo):
            koliko += 1
        kvocient = koliko / stevilo
        stevilo += 1
    return stevilo - 1

