import os

try:
    a = int(input("Podaj liczbe a: "))
    b = int(input("Podaj liczbe b: "))
    c = ((a+b)//(a-b))
except ZeroDivisionError:
    print("a/b result in 0")
else:
    print(c)

try:
    k = 5/0
    print(k)
except ZeroDivisionError:
    print("Can't divide by zreo")
finally:
    print('This is always executed')

#zadanie 1
try:
    age = int(input("Wprowadź wiek: "))
except ValueError:
    print("Oczekiwana liczba całkowita")
    age = int(input("Wprowadź wiek ponownie: "))

#zadanie 2
def convert_to_integer(string):
    try:
        convert = int(string)
    except ValueError:
        print("Oczekiwana liczba całkowita")
    except Exception as e:
        print(str(e))
    else:
        print(convert)

convert_to_integer('kk')

#zadanie 1
inputFile = input("Podaj plik wejściowy: ")
outputFile = input("Podaj plik wyjsciowy: ")

try:
    with open(inputFile) as f:
        lines = len(f.readlines())
        print("Iloszć linji:", lines)
        f.close()
        with open(outputFile, 'w') as f1:
            f1.write(str(inputFile))
            f1.write(" ")
            f1.write(str(lines))
            f1.close()
except Exception as e:
    print(str(e))

#zadanie 2
def find_word(file_path, word):
    if not os.path.exists(file_path):
        return False
    try:
        with open(file_path) as f:
            for line in f:
                if line.__contains__(word):
                    f.close()
                    return True
            f.close()
    except Exception as e:
        print(str(e))
        return False
    else:
        return False

print(find_word("les10_test_file_output.txt", "les10_test_file"))

#zadanie 3
def append_to_file(file_path, text):
    try:
        with open(file_path, 'a') as f:
            f.write(text)
            f.close()
    except Exception as e:
        print(str(e))

append_to_file("les10_test_file.txt", "Test text 10")

#zadanie 4
filePath = input("Podaj file: ")
try:
    with open(filePath) as f:
        with open("wynik.txt", 'w') as f1:
            for line in f:
                f1.write(line.upper())
            f1.close()
        f.close()
except FileNotFoundError:
    print("Plik na scierzce {0} nie istneje".format(filePath))
except Exception as e:
    print(str(e))

#zadanie 5
def delete_file(file_path):
    try:
        os.remove(file_path)
        print("Plik został usunienty")
    except FileNotFoundError:
        print("Plik na scierzce {0} nie istneje".format(file_path))
    except Exception as e:
        print(str(e))

delete_file("deletest.txt")
