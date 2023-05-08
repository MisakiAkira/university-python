import random

list=[random.randrange(1,201) for i in range(20)]
print([i for i in list if i%2==0 and i%5==0])

print(sum([i for i in list if i < 50]))

#imiona=[input("Podaj imie: ") for i in range(5)]
#dlugosc=[len(i) + "={i}" for i in imiona]
#print(dlugosc)

numbers=[i*5 for i in range(1,7)]
print(numbers)
#print([i*5 for i in range(1,7)])
 
info=[input("Podaj imie i zarobhi w postaci 'imie:zarobki'\n") for i in range(5)]
print([x for x in info if x.split(':')[1] == max([i.split(':')[1] for i in info])][0])
