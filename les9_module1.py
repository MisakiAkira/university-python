def czy_palindrom(napis):
    for i in range(len(napis)):
        if napis[i] != napis[len(napis) - 1 - i]:
            return False
    return True

def ile_spolglosek(napis):
    samogloski = "eyuioa"
    count = 0
    for letter in napis:
        if letter not in samogloski:
            count += 1
    return count

def swapcase(napis):
    return napis.swapcase()

def znak_w_krotkie(napis):
    return(tuple([letter for letter in napis]))