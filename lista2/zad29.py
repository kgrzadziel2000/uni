#import itertools


a = [[2,4,3],[1,5,6],[9],[7,9,0]]

b=a[0]
c=a[1]
d=a[2]
e=a[3]

a=[]
a.extend(b)
a.extend(c)
a.extend(d)
a.extend(e)
print(a)