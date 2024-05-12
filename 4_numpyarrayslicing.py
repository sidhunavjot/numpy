# slicing : it means taking elemnets from one index to another index

# [start : end], [start : end : step]

# slice values from 1 to 5

import numpy as np
x = np.array([1,2,3,4,5,6,7,8,9,0])
print(x[3:7])

# slice from 4th index to last value

import numpy as np
y = np.array([2,3,4,5,6,7,8,9,0,9,8,7,6,5,4,3,2])
print(y[5:])

# slicing from start to 6th value

import numpy as np
z = np.array([2,3,4,5,6,7,8,9,0,0,9,8,7,7,7,6,5,4,3,2,1])
print(z[:7])


# negative slicing index -3

import numpy as np
z = np.array([2,3,4,5,6,7,8,9,0,0,9,8,7,7,7,6,5,4,3,2,1])
print(z[-3:-1])

# step: you will use step value to determine the step of the slicing
# return every value with steps

import numpy as np
z = np.array([2,3,4,5,6,7,8,9,0,0,9,8,7,7,7,6,5,4,3,2,1])
print(z[1:5:2])

# to getn even/odd values without giving start or end value
#  return every other number from the entire array

import numpy as np
z = np.array([2,3,4,5,6,7,8,9,0,0,9,8,7,7,7,6,5,4,3,2,1])
print(z[::2])

# slicing 2-D array : print 8,7

import numpy as np
a = np.array([[2,3,4,5,6],[9,8,7,6,5]])
print(a[1,1:3])

# slicing by taking values from both : 2nd index of both arrays

import numpy as np
a = np.array([[2,3,4,5,6],[9,8,7,6,5]])
print(a[0:2, 2])

# slicing 2D - PRINT FFROM BOTH INDEX 1:4

import numpy as np
a = np.array([[2,3,4,5,6],[9,8,7,6,5]])
print(a[0:2, 1:4])


