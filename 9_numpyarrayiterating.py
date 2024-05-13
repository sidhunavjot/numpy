# iterating means going through the elements one by one or step by step. like for loop.

 # iterate the element of 1-D

import numpy as np
x = np.array([1,2,3])
for i in x:
    print(i)

# iterate in 2-D

import numpy as np
x = np.array([[1,2,3],[4,5,6]])
for i in x:
    print(i)

# Iterate on each Scalar element of the 2-D

import numpy as np
x = np.array([[1,2,3],[4,5,6]])
for i in x:
    for j in i:
        print(j)
print("2-D finished")

# Iterate on each Scalar element of the 3-D

import numpy as np
x = np.array([[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]])
for i in x:
    for j in i:
        for k in j:
            print(k)
print("3-D finished  first")

# Iterating arrays using nditer() funtion
# we will iterate on each scalar element

import numpy as np
x = np.array([[[1,2],[4,5],[7,8],[10,11]]])
for i in np.nditer(x):
    print(i)

print("3-D finished with nditer")

# iterating with STEPS

import numpy as np
x = np.array([[[1,2],[4,5],[7,8],[10,11]]])
for i in np.nditer(x[:,::2]):
    print(i)

print("3-D finished with nditer STEPS")

# iterating with STEPS two

import numpy as np
x = np.array([[1,2,3,4],[5,6,7,8]])
for i in np.nditer(x[:,::2]):
    print(i)

print("3-D finished with nditer STEPS TWO")


