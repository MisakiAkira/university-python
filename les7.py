import math

class Book:
    def __init__(self, title, numOfPages, author, yearOfPublish, owner):
        self.title = title
        self.numOfPages = numOfPages
        self.author = author
        self.yearOfPublish = yearOfPublish
        self.owner = owner
    def getInfo(self):
        return "Title: {}, number of pages: {}, author: {}, year of publishing: {}, owner: {}".format(self.title, self.numOfPages, self.author, self.yearOfPublish, self.owner)
    def changeOwner(self, newOwner):
        self.owner = newOwner

book = Book('title', 12, 'asd', 2018, 'me')
print(book.getInfo())
book.changeOwner('not me')
print(book.getInfo())
book1 = Book('Any', 15, 'affjafaf', 1292, 'me')

books = [book, book1,]
print([bookinfo.getInfo() for bookinfo in books])

class FunkcjaKwadratowa:
    def __init__(self, a = 0, b = 0, c = 0):
        self.a = a 
        self.b = b
        self.c = c
    def rozwiaz(self):
        d = self.b * self.b - 4 * self.a * self.c
        if d < 0:
            return 'Nie ma razwiązań'
        elif d == 0:
            return "Tylko jedno rozwiązanie: {}".format((-self.b)/(2*self.a))
        else:
            return "Rozwiązania: {} : {}".format((-self.b - math.sqrt(d))/(2*self.a), (-self.b + math.sqrt(d))/(2*self.a))

f = FunkcjaKwadratowa(2, 3, 1)
print(f.rozwiaz())

class Jednoslad:
    def __init__(self, ps, kolor, marka, sb):
        self.ps = ps
        self.kolor = kolor
        self.marka = marka
        self.sb = sb
    def uruchom(self):
        return 'Został uruchamiony'
    def changeSb(self, sb):
        self.sb = sb

class Skuter(Jednoslad):
    def skuterUniqueMethod(self):
        return 'This method is unique for skuter'

class Motocykl(Jednoslad):
    def __init__(self, ps, kolor, marka, sb):
        Jednoslad.__init__(self, ps, kolor, marka, sb)
    def motoUniqueMethod(self):
        return 14

skut = Skuter(1,1,1,1)
skut.changeSb(4)
print(skut.skuterUniqueMethod())
moto = Motocykl(2,2,2,2)
print(moto.motoUniqueMethod())

class Pojazd:
    def __init__(self, nazwa, rodzaj, kolor, wartosc):
        self.nazwa = nazwa
        self.rodzaj = rodzaj
        self.kolor = kolor
        self.wartosc = wartosc

auto1 = Pojazd('Ferrari', 'kabriolet', 'czerwony', 60000)
auto2 = Pojazd('Ikarus', 'autobus', 'niebieski', 10000)
