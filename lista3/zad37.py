N = input()
Z = int(N)
q = 1
p = 0
print('0')
while p < Z:
    temp = q;
    q = p;
    p = temp + q;
    print(p);