import random
wrozba=random.randrange(5)
if wrozba==0:
    print("Dziśaj będzie fajny dzień")
elif wrozba==1:
    print("Dziśa będzie gorzy dzień")
elif wrozba==2:
    print("Czekaj na pieniędzy")
elif wrozba==3:
    print("Nie czekaj na pieniędzy")
else:
    print("Hallo")

orzelki=0
reszki=0
for i in range(100):
    if random.randrange(2)==0:
        orzelki+=1
    else:
        reszki+=1
print("Orzelki:", orzelki, "\nReszki:", reszki)

randomnumb=random.randrange(100)+1
for i in range(5):
    answer=-1
    while answer not in range(1,100):
        answer=(int)(input("Podaj liczbe\n"))
    if answer==randomnumb:
        print("Poprawnie")
        i=1000
    if i==4:
        print("Komputer zagadnoł liczbe:", randomnumb)

uzytkownik=[]
komputer=[]
for i in range(6):
    liczb=-1
    while liczb not in range(1,49):
        liczb=(int)(input("Podaj liczbe w przedzale 49\n"))
    uzytkownik.append(liczb)
    komputer.append(random.randrange(49)+1)
for i in uzytkownik:
    if komputer.__contains__(i):
        print("Komputer losował",i)
    else:
        print(i,"nie wystarcza w liscie komputerza")
