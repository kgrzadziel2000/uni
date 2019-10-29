M = input("Wiersze=")
m = int(M)
N = input("Kolumny=")
n = int(N)
y = 1
while y < m+1:
    x = 1
    while x < n+1:
        print("%4d"%(y * x),end='')
        x += 1
    print()
    y += 1
