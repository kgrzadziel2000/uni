import math
import cmath
d=input()
x=input()
z=complex(d,x)
r=(((z.real)**2)+((z.imag)**2))**(1/2)         #(d**2+x**2)**(1/2)
e=cmath.phase(z)      #z=r(math.cos(x*math.pi/180)+((-1)**(1/2))*math.sin(x*math.pi/180))
z.conjugate()
print(z,r,e,z.conjugate())