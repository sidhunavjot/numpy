# shape of array is the number of elements in each dimensions

# get shape of any array

import numpy as np

x = np.array([[1,2,3,4],[5,6,7,8]])
print(x.shape)

# 5D array with ndim

import numpy as np

x = np.array([[1,2,3,4]], ndmin=5)
print(x)
print(x.shape)

