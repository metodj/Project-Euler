def prastevilo(n):
    s = 0
    for i in range(2,int(n**(1/2))+1):
        if n % i == 0:
            s += 1
    if s == 0:
        return True
    else:
        return False




def euler7(n):
    seznam = [2]
    for i in range(3,200000,2):
        if prastevilo(i) == True:
            seznam.append(i)
    return seznam[n-1]

def euler7_while(n):
    seznam = [2]
    i = 3
    while len(seznam)<n:
        if prastevilo(i) == True:
            seznam.append(i)
        i += 2
    return seznam[n-1]


