#zadanie 1
imiona = ["Alex", "Kszystow", "Ala", "Mateusz",]
print(imiona)
imie=input("Które imie zmienić?\n")
imiona[imiona.index(imie)]=input("Wprowadż nowe imię.\n")
print(imiona)

#zadanie 2
print(imiona)
imiona.sort()
print(imiona)

#zadanie 3
print(imiona)
imie=input("Usuwane imie?\n")
imiona.remove(imie)
print(imiona)

del imiona

#zadanie 4
imiona=('Jakub','Bartosz','Max','Filip')
print(imiona)
imionatemp=(list)(imiona)
imionatemp.sort()
imiona=(tuple)(imionatemp)
print(imiona)

#zadanie 5
krotka=(1,2,3,4,5,)
print(krotka)
print(sum(krotka))

#zadanie 6
pocket=('pen','pencil','keys')
print(pocket)
print('keys' in pocket)
print(len(pocket))
print(pocket[:-2])
add=('coins',)
#nie da sie dodacz do krotki nowych elementów
largerpocket=pocket+add
print(largerpocket)
