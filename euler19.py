def days(month, year):
    if month == 9 or month == 4 or month == 11 or month == 6:
        return 30
    elif month == 2:
        if year % 4 == 0 and year % 100 != 0:
            return 29
        if year % 400 == 0:
            return 29
        return 28
    else:
        return 31

ime_dneva = ['pon', 'tor', 'sre', 'cet', 'pet', 'sob', 'ned']

def euler19():
    stevec, koliko_nedelj = 1, 0 #1901 se je zacel s torkom
    for year in range(1901, 2001):
        for month in range(1, 13):
            for dan in range(1, days(month,year) + 1):
                ime = ime_dneva[stevec]
                if ime == 'ned' and dan == 1:
                    koliko_nedelj += 1
                stevec += 1
                if stevec >= 7:
                    stevec = 0
    return koliko_nedelj


print('Število nedelj:', euler19())