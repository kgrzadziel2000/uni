import math


A = input("a=")
a = int(A)

B = input("b=")
b = int(B)

C = input("c=")
c = int(C)

if a == 0:
    print("Równanie nie jest kwadratowe")
delta = (b*b)-(4*a*c)
print("Delta=",delta)
if delta<0:
    print("Delta mniejsza od zero, brak rozwiązań.")
else:
    if delta == 0:
        x = (-b)*(2*a)
        print(x)
    else:
        print("Pierwiastek z delty=",math.sqrt(delta))
        x1 = ((-b) - (math.sqrt(delta))) / (2 * a)
        x2 = ((-b) + (math.sqrt(delta))) / (2 * a)
        print("X1=", x1, "        ", "X2=", x2)