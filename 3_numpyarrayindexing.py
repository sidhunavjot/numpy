# Array indexing is the same as accessing an array element. start with 0, second 1

import numpy as np
a = np.array([1,2,3,4])
print(a[2])

# we can get 3rd and 4rth element by adding

import numpy as np
b = np.array([1,2,3,4,5])
print(a[2] + a[3])

# accessing 2-D it is like a row and columns

import numpy as np
c = np.array([[1,2,3,4,5],[5,6,7,8,9]])
print(c[0,1]) # find 2nd element of 1st row

# accessing the 3-D Model

import numpy as np
x = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(x[1])
print(x[1,1])
print(x[1,1,1])

