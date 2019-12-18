import numpy as np
import matplotlib as mpl

a = np.array([[1,2,3,-2,-1], [3,5,5,-3,-9],[2,3,2,0,-8],[2,6,7,-5,1],[1,2,6,-4,-10]])
b = np.array([6,2,-5,17,12])
x = np.linalg.solve(a, b)
print("\nx= "+str(x[0])+"\ny= "+str(x[1])+"\nz= "+str(x[2])+"\nt= "+str(x[3])+"\nu= "+str(x[4])+"\n")

#x + 2y + 3z−2t−u = 6 
#3x + 5y + 5z−3t−9u = 2 
#2x + 3y + 2z−8u = −5 
#2x + 6y + 7z−5t + u = 17 
#x + 2y + 6z−4t−10u = 12 