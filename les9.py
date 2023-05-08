import les9_module as myModule1
import les9_module1 as myModule2
from les9_katalog.module_in_katalog import pole

print(myModule1.czy_liczba("123"))

list = [15, 20, 1, 46, -3, 77, 82,]

#zadanie 1

print(myModule1.min_from_list(list))

#zadanie 2

napis = input("Podaj napis do metod\n")

print(myModule2.czy_palindrom(napis))

print(myModule2.ile_spolglosek(napis))

print(myModule2.swapcase(napis))

print(myModule2.znak_w_krotkie(napis))

#katalog przyklad

print(pole(3, 7))

#pakiety
from les9_pakiet_liczby import module1
from les9_pakiet_liczby import module2
from les9_pakiet_liczby import module3

print(module1.iloczyn(7854))

print(module2.tablica_mnozenia(15))

module3.liczba_doskonala_in_range()
