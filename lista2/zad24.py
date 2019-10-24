print("Wpisz słowo które zamierzasz zmienić:")
x = input()
q=x[0]
z=x.replace(q,"$")
t=list(z)
t[0]=x[0]
u=''.join(t)
print(u)