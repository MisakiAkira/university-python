import sqlite3

# con = sqlite3.connect('baza.db')
# # con.row_factory = sqlite3.Row
# cur = con.cursor()

# cur.execute("DROP TABLE IF EXISTS klasa")
# cur.execute("""
# CREATE TABLE IF NOT EXISTS klasa(
#     id INTEGER PRIMARY KEY ASC,
#     nazwa varchar(250) NOT NULL,
#     profil varchar(250) DEFAULT ''
# )""")
# cur.executescript("""
# DROP TABLE IF EXISTS uczen;
# CREATE TABLE IF NOT EXISTS uczen(
#     id INTEGER PRIMARY KEY ASC,
#     imie varchar(250) NOT NULL,
#     nazwisko varchar(250) NOT NULL,
#     klasa_id INTEGER NOT NULL,
#     FOREIGN KEY(klasa_id) REFERENCES klasa(id)
# )""")

# cur.execute('INSERT INTO klasa VALUES(NULL, ?, ?);', ('1A', 'matematyczny'))
# cur.execute('INSERT INTO klasa VALUES(NULL, ?, ?);', ('1B', 'humanistyczny'))

# cur.execute('SELECT id FROM klasa WHERE nazwa = ?', ('1A',))
# klasa_id = cur.fetchone()[0]
# print(klasa_id)

# uczeniowe = (
#     (None, 'Tomasz', 'Nowak', klasa_id),
#     (None, 'Jan', 'Kos', klasa_id),
#     (None, 'Piotr', 'Kowalski', klasa_id)
# )
# cur.executemany('INSERT INTO uczen VALUES(?, ?, ?, ?)', uczeniowe)
# con.commit()

# uczeniowe = cur.execute("""
# SELECT uczen.id, imie, nazwisko, nazwa FROM uczen, klasa
# WHERE uczen.klasa_id = klasa.id
# """).fetchall()

# print(uczeniowe)

# con.close()

con = sqlite3.connect('baza2.db')
# con.row_factory = sqlite3.Row
cur = con.cursor()

cur.executescript("""
DROP TABLE IF EXISTS hotel;
CREATE TABLE hotel(
    id INTEGER PRIMARY KEY ASC,
    nr_pokoju INTEGER NOT NULL
);

DROP TABLE IF EXISTS gosc;
CREATE TABLE gosc(
    id INTEGER PRIMARY KEY ASC,
    imie varchar(250) NOT NULL,
    nazwisko varchar(250) NOT NULL,
    ile_dni INTEGER NOT NULL
);

DROP TABLE IF EXISTS uwagi;
CREATE TABLE uwagi(
    id INTEGER PRIMARY KEY ASC,
    uwagi varchar(250) NOT NULL,
    gosc_id INTEGER NOT NULL,
    FOREIGN KEY(gosc_id) REFERENCES gosc(id)
)""")
con.commit()

print('HEllo world!')

con.close()
