x = input()
y = int(x)
z = y % 2

while z==0:
    print("Parzysta")
    z+=2

while z==1:
    print("Nieparzysta")
    z+=2

#Dodajemy o 2 a nie o jeden gdyż w wypadku dodania o jeden z=1
#co uruchamia drugą pętlę, można to łatwo naprawić zamieniając miejscami pętle.
#Jednakże dodanie o 2 jest jeszcze łatwiejszą naprawą.