def liczba_doskonala_in_range(first = 1, last = 100):
    if first > last:
        print("First can't be greater than last")
        return
    for liczba in range(first, last + 1):
        dzielniki = [dzielnik for dzielnik in range(1, liczba) if liczba % dzielnik == 0]
        if sum(dzielniki) == liczba:
            print("{} is doskonala".format(liczba))
