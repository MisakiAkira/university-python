import math
import sqlite3

#zadanie 1
file = input("Wprowadz nazwe pliku\n")
try:
    with open(file) as f:
        lines = f.readlines()
        for line in lines:
            if len(line) > 40:
                print(line)
except Exception as e:
    print(str(e))

#zadanie 2
w = 10.2
x = 1.3
y = 2.8
z = 17.5
dna1 = 'attattaggaccaca'
dna2 = 'attattaggaacaca'
species1 = 'diplodocus'
species2 = 'tyrannosaurus'
try:
    print('w jest większy niż 10:' ,w > 10)
    print('w+x jest mniejszy niż 15:', (w + x) > 15)
    print('x jest większy niż y:', x > y)
    print('2*x+0,2 jest równe y:', round((2 * x + 0.2), 3) == y)
    print('dna1 jest taki sam jak dna2:', dna1 == dna2)
    print('dna1 nie jest tym samym co dna2:', dna1 == dna2)
    print('Liczba wystąpień t jest taka sama w dna1 i dna2:', dna1.count('t') == dna2.count('t'))
    print('x razy w między 13,2 a 13,5:', 13.2 <= (x * w) <= 13.5)
    print('species2 występuje przed species1 alfabetycznie:', sorted([species1, species2,], key = str.lower) == species2)
    print('w jest większy niż x i y jest większy niż z:', w > x and y > z)
    print('Łączna długość dwóch sekwencji DNA jest większa lub równa 30:', (len(dna1) + len(dna2)) >= 30)
    print('(w+x+y) podzielone przez logarytm (podstawa 10) ze 100 równa się 7,15:', (w + x + y)/math.log10(100) == 7.15)
except Exception as e:
    print(str(e))

#zadanie 3
con = sqlite3.connect('les12.db')
con.row_factory = sqlite3.Row
cur = con.cursor()

cur.executescript("""
DROP TABLE IF EXISTS Hospital;
CREATE TABLE Hospital(
    Hospital_Id INTEGER PRIMARY KEY ASC,
    Hospital_Name varchar(250) NOT NULL,
    Bed_Count INTEGER NOT NULL
);
DROP TABLE IF EXISTS Doctor;
CREATE TABLE Doctor(
    Doctor_Id INTEGER PRIMARY KEY ASC,
    Doctor_Name varchar(250) NOT NULL,
    Hospital_Id INTEGER NOT NULL,
    Joining_Date DATETIME NOT NULL,
    Speciality varchar(250) NOT NULL,
    Salary INTEGER NOT NULL,
    Experience varchar(250) NOT NULL,
    FOREIGN KEY(Hospital_Id) REFERENCES Hospital(Hospital_Id)
)
""")

szpitale = (
    (None, 'Marii Kuri', 120),
    (None, 'Franciszka Boguszewicza', 300),
    (None, 'Jesusa', 5000)
)

lekarzy = (
    (None, 'Jesus Crist', 3, '1999-12-13', 'Surgeon', 100000, 'Pracuje od 0AD'),
    (None, 'Marcin Kowalski', 2, '2004-06-03', 'Doctor', 10000, 'Jakis'),
    (None, 'Adam Karpacki', 1, '2003-08-30', 'Nurse', 1000, 'None'),
    (None, 'Maria Edengauser', 2, '1989-10-01', 'Chief', 100000, 'Abbba'),
    (None, 'Hanz Gigender', 3, '2010-01-01', 'Chemist', 10000, 'Po uniwersytecie'),
    (None, 'Daniil Migirow', 1, '1888-03-10', 'Nurse', 1000, 'None')
)

cur.executemany('INSERT INTO Hospital VALUES(?, ?, ?)', szpitale)
cur.executemany('INSERT INTO Doctor VALUES(?, ?, ?, ?, ?, ?, ?)', lekarzy)
con.commit()

szpitale = cur.execute('SELECT * FROM Hospital').fetchall()
for szpital in szpitale:
    print('Identyfikator szpitala:', szpital['Hospital_Id'], '\nNazwa szpitala:',
    szpital['Hospital_Name'], '\nLiczba łóżek:', szpital['Bed_Count'], end='\n\n')
print()

lekarzy = cur.execute('SELECT * FROM Doctor').fetchall()
for lekarz in lekarzy:
    print('Numer identyfikacyjny lekarza:', lekarz['Doctor_Id'], '\nImię lekarza:',
    lekarz['Doctor_Name'], '\nIdentyfikator szpitala:', lekarz['Hospital_Id'],
    '\nData Przystąpienia:', lekarz['Joining_Date'], '\nSpecjalność:',
    lekarz['Speciality'], '\nWynagrodzenie:', lekarz['Salary'],
    '\nDoświadczenie:', lekarz['Experience'], end='\n\n')

con.close()

#zadanie 4
file = input('Podaj nazwe pliku\n')

try:
    with open(file) as f:
        lines = f.read()
        coKtore = int(input('Co które słowo?\n'))
        words = lines.split()
        wordsToFile = words[::coKtore]
        if len(wordsToFile) >= 100:
            words1 = wordsToFile[:len(wordsToFile)//2]
            words2 = wordsToFile[len(wordsToFile)//2:]
            with open('les12words1.txt', 'w') as f1:
                for word in words1:
                    f1.write(word + '\n')
            with open('les12words2.txt', 'w') as f1:
                for word in words2:
                    f1.write(word + '\n')
        else:
            with open('les12words.txt', 'w') as f1:
                for word in wordsToFile:
                    f1.write(word + '\n')
except Exception as e:
    print(str(e))
