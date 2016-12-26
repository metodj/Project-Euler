def prastevilo(n):
    s = 0
    for i in range (2, int(n**(1/2))+1):
        if n % i == 0:
            s += 1
    if s == 0:
        return True
    else:
        return False



def euler3(n):
    resitev = []
    for i in range(1, int(n**(1/2))+1):
        if n % i == 0:
            if prastevilo(i) == True:
                resitev.append(i)
    return max(resitev)

