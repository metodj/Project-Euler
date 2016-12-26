def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)

def factorial_for(n):
    s = 1
    for i in range(1, n+1):
        s *= i
    return s

def euler34(upper_limit):
    s = 0
    resitev = 0
    for i in range (144, upper_limit + 1):
        m = i
        while i > 0:
            s += factorial_for(i % 10)
            i //= 10
        if s == m:
            resitev += m
        s = 0
    return resitev




