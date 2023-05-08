s=["1", "2", "3", "4", "5"]
print(s[2:])
print(s[::2])
print(s[2::2])
print(s[::3])
print(s[2::3])
print(s[1:4])

s.append("6")
print(s[:])

s.insert(3, "halo")
print(s[:])

s1=["7", "8", "9"]
s.extend(s1)
print(s[:])

s2 = s + s1
print(s2)

print(3*s)
print(s)

x=["1", "2", "3"]
print(x)
x.append("4")
print(x)
x.insert(1, "halo")
print(x)

x=["1", "2", "3"]
print("Mamy tablice:\n", x)

#x.insert((int)(input("gdzie wstawić element?\n")), input("co wstawić?\n"))
print(x)

print(s)
s[3] = "Nie halo:("
print(s)

s[0:3] = ["-1", "-2", "-3"]
print(s)

print(x)
#index = (int)(input("Gdzie zmienić?\n")) - 1
#x[index] = input("Czego wstawić?\n")
print(x)

print(s)
s.reverse()
print(s)
s.sort()
print(s)

v1=["1", "2"]
v2=["2", "0"]
print(v1<v2)

print("1" in v2)

print(v1.pop(0))
del v1[0]
print(v1)
print(v2)
v2.remove("0")
print(v2)
v2.append("|")
v2.append("2")
v2.remove("2")
print(v2)

liczby =[(int)(input()), (int)(input()), (int)(input()), (int)(input())]
print(liczby)
print(sum(liczby))
