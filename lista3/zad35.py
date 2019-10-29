import re
z=0 # "z" zapisuje ilość brakujących rzeczy, jeśli na końcu programu będzie różne od 0, zostanie wyświetlona wiadomość, że hasło jest niepoprawne.
x = input("Hasło=")
if len(x)>16:
    print("Hasło za długie")
    z+=1
    quit
if len(x)<6:
    z+=1
    print("Hasło za krótkie")
    quit
Alph_m = re.findall("[a-z]", x)
Alph_d = re.findall("[A-Z]", x)
Liczba = re.findall("[0-9]", x)
Znaki = re.findall("[$#@]", x)
if (Alph_m):
    pass
else:
    if (Alph_d):
        pass
    else:
        z+=1
        print("Brakuje litery")
        quit
if (Liczba):
    pass
else:
    z+=1
    print("Brakuje liczby")
    quit
if (Znaki):
    pass
else:
    z+=1
    print("Brakuje jednego ze sprecyzowanych znaków specjalnych")
    quit
if z == 0:
    print("HASŁO POPRAWNE")