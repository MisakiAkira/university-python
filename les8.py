#zadanie 1
daneList = ['imie','date urodzenia','adres email','numer telefonu',]
for i in daneList:
    daneList[daneList.index(i)] = input("Wprowadz: {}\n".format(i))

daneTuple = ([i for i in daneList])

daneSlownik ={
    daneList[0]: (daneList[1], daneList[2], daneList[3])
}

for i in daneList:
    print(i)
for i in daneTuple:
    print(i)
for i in daneSlownik:
    print(i, daneSlownik[i])

#zadanie 2
class Product:
    def __init__(self, nr, nazwa, ilosc, cena):
        self.nr = nr
        self.nazwa = nazwa
        self.ilosc = ilosc
        self.cena = cena
    def info(self):
        return "{}\t{}\t{}\t{}".format(self.nr,self.nazwa,self.ilosc,self.cena)
    def changeNazwa(self, nazwa):
        self.nazwa = nazwa
    def changeIlosc(self, ilosc):
        self.ilosc = ilosc
    def changeCena(self,cena):
        self.cena = cena

count = 1
productList = []

def show():
    print("Nr\tNazwa\tIlosc\tCena")
    for i in productList:
        print(i.info())

def add(count):
    productList.append(Product(count,input("Podaj nazwe\n"),input("Podaj ilosc\n"),input("Podaj cene\n")))

def modify():
    show()
    x = int(input("Podaj numer productu na modyfikacje\n"))
    p = object
    for i in productList:
        if i.nr == x:
            p = i
            productList.remove(i)
    if p == object:
        return
    x = int(input("Czego modyfikować?\n1 - nazwa\n2 - ilosc\n3 - cena\n0 - remove\n"))
    if x == 0:
        return
    elif x == 1:
        p.changeNazwa(input("Podaj nawą nazwe\n"))
        productList.append(p)
    elif x == 2:
        p.changeIlosc(input("Podaj nawą ilosc\n"))
        productList.append(p)
    elif x == 3:
        p.changeCena(input("Podaj nawą cene\n"))
        productList.append(p)
    else:
        print("Błędny wariant")
        productList.append(p)

loop = True
while(loop):
    x = int(input("1 - show list\n2 - add product\n3 - modify\n0 - exit\n"))
    if x == 0:
        loop = False
    elif x == 1:
        show()
    elif x == 2:
        add(count)
        count=count+1
    elif x == 3:
        modify()
    else:
        print("Błędny wariant")

#zadanie 3
a = 3
b = 4
for i in range(a):
    for j in range(b):
        print("* ",end="")
    print()
print("Pole = {}, obwód = {}".format(a*b,2*(a+b)))

#zadanie 4
x = int(input("Podaj liczbę\n"))
if x < 0:
    x = -x
print("Wartośc bezwzględna: {}".format(x))

#zadanie 5
a = -1
b = -1
c = -1
while a < 0:
    a = int(input("Podaj a, więcej od zera:\n"))
while b < 0:
    b = int(input("Podaj b, więcej od zera:\n"))
while c < 0:
    c = int(input("Podaj c, więcej od zera:\n"))

if a * a + b * b == c * c:
    print("Liczby {}, {} i {} są trójkami pitagorejskimi".format(a,b,c))
else:
    print("Liczby {}, {} i {} nie są trójkami pitagorejskimi".format(a,b,c))

#zadanie 6
x = 1
y = 7
sum = 0
for i in range(x,y+1):
    if i % 2 != 0:
        sum += i
print("Suma liczb nie parzystych na ciągu od {} do {} są {}".format(x,y,sum))

#zadanie 7
print(str(input("Podaj tekst\n")).upper())

#zadanie 8
a = int(input("Licba w systemie dwójkowym:\n"),2)
b = int(input("Liczba w systemie ósemkowym:\n"),8)
c = int(input("Liczba w systemie szesnastkowym:\n"),16)

print(a,b,c)

#zadanie 9
string_maps = {
 "1": "abc",
 "2": "def",
 "3": "ghi",
 "4": "jkl",
 "5": "mno",
 "6": "pqrs",
 "7": "tuv",
 "8": "wxy",
 "9": "z"
}
x = int(input("Podaj dwucyfrową liczbę\n"))
if x > 9 and x < 100:
    des = int(x / 10)
    jed = int(x % 10)
    print(["{}{}".format(i,j) for i in string_maps[str(des)] for j in string_maps[str(jed)]])
else:
    print("Błędna liczba")

#zadanie 10
banknots = {
    1:"Jerzego Waszyngtona",
    2:"Thomas Jefferson",
    5:"Abrahama Lincolna",
    10:"Aleksandra Hamiltona",
    20:"Andrzeja Jacksona",
    50:"Ulyssesa S. Granta",
    100:"Benjamin Franklin"
}
x = int(input("Podaj baknotę\n"))
if banknots.__contains__(x):
    print(banknots[x])
else:
    print("Nie ma takiej banknoty")

#zadanie 11
def translate(text):
    