def czy_liczba(napis):
    return napis.isnumeric()

def min_from_list(list):
    min = list[0]
    for item in list:
        if item < min:
            min = item
    return min