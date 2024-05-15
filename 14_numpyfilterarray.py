# Getting some elements out of an existing array and creating a new array is called filtering.

# a boolean index list is a list of boolean corresponding to indexes in the array.

# create an array from the element on index 0 to 2

import numpy as np
x = np.array([42,43,55,67])
x1 = np.array([True,False,True,False])

y = x[x1]
print(y)

# create a filter array
# that returns values above xyz value

import numpy as np
x = np.array([42,43,55,67])
y = []

for i in x:
    if i > 43:
        y.append(True)
    else:
        y.append(False)

z = x[y]
print(z)

# create a filter array that will return only even elements from the original array.

import numpy as np
x = np.array([42,43,55,67])
y = []

for i in x:
    if i%2==0:
        y.append(True)
    else:
        y.append(False)
z = x[y]
print(z)

# you can create filter directly from array

 
import numpy as np
x = np.array([42,43,55,67])
y = x > 42
z = x[y]
print(y)
print(z)
