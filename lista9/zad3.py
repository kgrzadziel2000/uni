from numpy import pi
import numpy as np
import matplotlib.pyplot as plt
import math

V0 = int(input("Podaj prędkość początkową: "))
a = int(input("Podaj kąt rzutu (w stopniach): "))


g=9.8

MAX_HEIGHT = (V0*V0*math.sin(a*pi/180)*math.sin(a*pi/180))/(2*g)
#ZASIEG = (2*V0*V0*math.sin(a*pi/180)*math.cos(a*pi/180))/g
ZASIEG2 = (V0*V0*math.sin(2*a*pi/180))/g
CZAS_UPADEK = 2*V0*math.sin(2*a*pi/180)

t = np.arange(0, CZAS_UPADEK, 0.2)
x = np.arange(0, CZAS_UPADEK, 0.2)
VX = V0*math.cos(a*math.pi/180)*(t-t+1) #VX stałe
VY = V0*math.sin(a*math.pi/180)-g*t
z= x*math.tan(a*math.pi/180)
m= (g*np.square(x))/(2*np.square(VX))
tor = z-m
d = V0*math.cos(a*math.pi/180)*t
f = V0*t-g*np.square(t)/2
c = np.sqrt(np.square(d)+np.square(f))

print("\nWysokość maksymalna to: "+str(MAX_HEIGHT)+"m")
#print(ZASIEG)
print("Zasięg wynosi: "+str(ZASIEG2)+"m")
print("Czas lotu wynosi: "+str(CZAS_UPADEK)+"s\n")


plt.subplot(311)
plt.plot([t], [VX], 'rs')
plt.plot([t], [VY], 'bo')
plt.axis([0, CZAS_UPADEK,0,VY[0]])
plt.xlabel('Czas t(sekundy)')
plt.ylabel('Prędkość VX/VY (m/s^2)')

plt.subplot(312)
plt.plot([t],[c], 'rs')
plt.xlabel('Czas t(sekundy)')
plt.ylabel('Odległość od [0,0]')

plt.subplot(313)
plt.plot([x], [tor], 'rs')
plt.xlabel('odległość x')
plt.ylabel('wysokość y')

plt.show()