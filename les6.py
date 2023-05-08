import math

def toupper():
    text = input("Podaj text\n")
    return text.upper()

#print(toupper())

def parz(list):
    return [i for i in list if i%2==0]

print(parz([1,2,3,4,5,6,7,8]))

def mileToKm(mile):
    return mile * 1609

print("3 mile jest:", mileToKm(3), "km")

def students(variant):
    if variant == 1:
        print(student)
    elif variant == 2:
        student.append(input("Wprowadż dane studenta\n"))
        students(1)
    else:
        print("Niepoprawny variant")

student = ["Jhon", "Mark", "Alice", "Kim"]

students(int(input("Podaj wariant\n")))


def zero(a,b,c):
    d = b*b-4*a*c
    if d < 0:
        print("Nie ma miejsca zerowego")
        return ""
    elif d == 0:
        return (-b)/(2*a)
    else:
        return (-b+math.sqrt(d))/(2*a), (-b-math.sqrt(d))/(2*a)
