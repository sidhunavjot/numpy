# we will create ndarray
# array object in numpy is called ndarray
# array()


#list
import numpy as np
x=np.array([1,3,4,67,9])
print(x)
print(type(x))

# we can also pass a list, tuple or any array like object with array()
# and it will be converted to ndarray

#tuples
import numpy as np
y = np.array((3,4,6,7,88,99,00))
print(y)
print(type(y))


# dimensions in array - a dimension in array is one level of array depth(nested array)
# 0-D Arrays - scalers, are the elements in an array, each value in an array is a 0-D array.


 # now we will create 0-D Array with value 42

import numpy as np
z= np.array(42)
print(z)


# 1-D arrays- an array that has 0-D arrays as its element is called uni directions+al or 1-D

import numpy as np
m = np.array([2,4,56,7])
print(m)

# create a 2-D  Array containing 2 darrays with certain values

# NOTE:- Keep size of array equal or say number of elements in each array should be equal

import numpy as np
n = np.array([[3,4,5,6],[8,3,4,5]])
print(n)


# create a 3-D array with two 2-D array

import numpy as np

o = np.array([[[3,4,1,4],[3,4,56,7]],[[2,3,4,2],[9,3,4,5]]])
print(o)



# check how many dimensions the array have ? : ndim attribute

import numpy as np
k = np.array(42)
l = np.array([2,4,56,7])
j = np.array([[3,4,5,6],[8,3,4,5]])
f = np.array([[[3,4,1,4],[3,4,56,7]],[[2,3,4,2],[9,3,4,5]]])

print(k.ndim)
print(l.ndim)
print(j.ndim)
print(f.ndim)

# create an array with 5 dimensions and verufy that it has 5 dimensions

import numpy as np
k = np.array([2,3,4,5,6], ndmin=5)
print(k)
print(k.ndim)






