import math

class kolo:
    def __init__(self, promien):
        self.r = promien

    def pole(self):
        P = math.pi*self.r**2
        print("Pole wynosi = "+str(P))
    
    def obwod(self):
        OB = 2*math.pi*self.r
        print("Obwód wynosi = "+str(OB))




#Testowanie czy działa
p1 = kolo(4)
p1.pole()
p1.obwod()