print("Wpisz słowo które zamierzasz zmienić:")
x = input()
list(x)
q = list(x)[0]
w = list(x)[1]
e = list(x)[-2]
r = list(x)[-1]
letters = []
letters.append(q)
letters.append(w)
letters.append(e)
letters.append(r)
finish = ''.join(letters)
print(finish)
