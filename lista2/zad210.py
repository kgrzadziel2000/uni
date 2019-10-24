x = []
z = range(3, 100, 3)
for y in z:
 x.append(y)

f = range(4,24,2)
for d in f:
    del x[d]
p=sum(x)
k=len(x)
t = p/k




print(t)


