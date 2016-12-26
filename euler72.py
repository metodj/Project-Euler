'''lep primer za naučiti 'sieve' metodo'''


seznam = list(range(2, 1000000 + 1))

def euler_72(seznam):
    limit = len(seznam)
    i = 2
    stevec_indeksov = 0

    while i < limit:
        if seznam[stevec_indeksov] == i:
            for veckratnik in range(stevec_indeksov, limit, i):
                seznam[veckratnik] *= (1 - 1 / i)
        i += 1
        stevec_indeksov += 1
    return int(sum(seznam))