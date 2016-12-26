def factorial_for(n):
    s = 1
    for i in range(1, n+1):
        s *= i
    return s

def euler20(n):
    resitev = 0
    for znak in str(factorial_for(n)):
        resitev += int(znak)
    return resitev

