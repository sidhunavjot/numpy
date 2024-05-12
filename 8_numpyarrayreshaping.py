# reshaping of array means changing the shape of an array, like adding or removing the elements

# reshaping from 1-D to 2-D

import numpy as np
x = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
x1 = x.reshape(4,3)
print(x)
print(x1)

# reshaping from 1-D to 3-D

import numpy as np
x = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
x1 = x.reshape(2,3,2)
print(x)
print(x1)

# NOTE: We can change only as per length of array

#return copy or view

import numpy as np
x = np.array([1,2,3,4,5,6,7,8])
print(x.reshape(2,4).base)

# unknown dimension - you are allowed only to have ONE unknown dimension. pass -1

import numpy as np
x = np.array([1,2,3,4,5,6,7,8])
x1 = x.reshape(2,2,-1)
print(x1)

# flattening the array by converting multidimensional into 1-D
# Note: simply pass -1 in reshape

import numpy as np
x = np.array([[1,2,3],[4,5,6]])
x1 = x.reshape(-1)
print(x1)

# NOTE : there are a lot of functions for changing the shapes of an array in numpy.
# like flatten, ravel and also rearranging the element rot90, flip, fliplr, flipud. 
# They come under advanced numpy






