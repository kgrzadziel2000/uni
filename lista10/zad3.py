import itertools as it

class zad3:
    def __init__(self, lista):
        self.lista = lista

    def zero(self):
        l = []
        z = it.combinations(self.lista, 3)
        for x in z:
            if int(sum(x)) == 0:
                l.append(x)
        print(l)




#Testowanie czy działa
p1 = zad3([-3,2,1,-2,0])
p1.zero()