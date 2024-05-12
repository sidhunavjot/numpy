# data types in python : string, integer, float, boolean, complex

# data type in numpy :
# i for integer
# b for boolean
# u for unasigned integer
# f for float
# c for complex float
# m for timedelta
# M for datetime
# O for object
# S for string
# U for unicode string
# V - memory

# checking the datatype of numpy array - dtype

import numpy as np
x = np.array([1,2,3,4])
print(x.dtype)

# checking data type of numpy array - string

import numpy as np
y = np.array(['a','b','c','d'])
print(y.dtype)

# creating array with deffined data type:

import numpy as np
z = np.array([1,2,3,4], dtype='S')
print(z)
print(z.dtype)

# create array with data type of 4 byte int

import numpy as np
k = np.array([1,2,3,4], dtype='i4')
print(k)
print(k.dtype)

# converting datatype in existing array - astype()

import numpy as np
k = np.array([1.1,2.1,3.1,4.1])
k = k.astype('i')
print(k)
print(k.dtype)

