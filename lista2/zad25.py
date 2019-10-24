print("Wpisz słowo które zamierzasz zmienić:")
x = input()
idx=len(x)//2
z=x[0:idx],'PYTHON',x[idx:]
u=''.join(z)
print(u)