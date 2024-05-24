# difference : use diff() function for finding the difference

# example : [1,2,3,4] the discrete difference of this would be [2-1, 3-2, 4-3] = [1,1,1] by ussing diff()


import numpy as np
x = np.array([10,15,25,5])
y = np.diff(x)
print(y)