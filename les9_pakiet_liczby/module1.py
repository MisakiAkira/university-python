def iloczyn(liczba):
    iloczyn = 1
    tmp = liczba
    while tmp > 1:
        tmplast = tmp % 10
        iloczyn = iloczyn * tmplast
        tmp = int(tmp / 10)
    return iloczyn
