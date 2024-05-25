# what is set ? a collection of unique elements.
# for creating the sets we use numpy unique() method to find the unique elements from any array.

# here we will convert the array with repeated elements in set

import numpy as np
x = np.array([2,2,2,3,4,4,3,4,4,6,2,2,1,1,6,6,6,7,7,8,9,4,0,0]) 
y = np.unique(x)
print(y)

# to find unique values of 2 1-d arrays we will use union1d() method

import numpy as np
x = np.array([2,2,3,4,5,6,7,8])
y = np.array([3,4,5,5,5,9,0,0])
z = np.union1d(x,y)
print(z)

# to find values that are present in both the arrays use intersect1d() function

import numpy as np
x = np.array([2,5,8,9,0])
y = np.array([3,2,5,6,7,0])
z = np.intersect1d(x,y, assume_unique=True)
print(z)

# to find the values that are present in the 1st set and NOT present in the 2nd set use, setdiff1d() funtion

import numpy as np
x = np.array([2,5,8,9,0])
y = np.array([3,2,5,6,7,0])
z = np.setdiff1d(x,y, assume_unique=True)
print(z)

# to find values that are NOT present in BOTH the sets, we use setxor1d() | uncommon elements means

import numpy as np
x = np.array([2,5,8,9,0])
y = np.array([3,2,5,6,7,0])
z = np.setxor1d(x,y, assume_unique=True)
print(z)



