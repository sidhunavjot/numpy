# ufunc - stands for unversal function and they are actually numpy functions that operates on the ndarray objects

# nfunc also takes additional arguments like, where, dtype and out.

# vectorization: converting the iterative statements into a vector based statement.

# example without ufunc, here we will use python in build zip()

x = [1,2,3,4]
y = [4,5,6,7]
z = []

for i,j in zip(x,y):
    z.append(i+j)
print(z)

# example with ufunc

import numpy as np

x = [1,2,3,4]
y = [4,5,6,7]
z = np.add(x,y)
print(z)