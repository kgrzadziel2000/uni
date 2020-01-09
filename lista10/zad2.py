import itertools as it

class permut:
    def __init__(self, lista):
        self.lista = lista
    
    def perm(self):
        t = 0
        l = []
        while(t<(len(self.lista)+1)):
            z = it.combinations(self.lista, t)
            t=t+1
            for x in z:
                l.append(x)
        print(l)
            


#Testowanie czy działa
p1 = permut([1,2,3])
p1.perm()