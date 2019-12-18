import numpy as np
import math

N = int(input("Podaj ile argumentów chcesz podać: "))
i = 0
arg = []
war = []
while (i < N):
    i+=1
    tmp = int(input("A"+str(i)+"= "))
    arg.append(tmp)

i = 0
suma=sum(arg)
sr = suma/len(arg)
for i in arg:
    tmp=i-sr
    tmp2 = tmp*tmp
    war.append(tmp2)
wari = sum(war)
waria = wari/len(war)
odch = math.sqrt(waria)

print("Średnia wynosi: "+str(sr))
print("Wariacja wynosi: "+str(waria))
print("Odchylenie standardowe wynosi: "+str(odch))