# summations : difference : addition is done between 2 arguments whereas summation happens over n elements.

# adding the 2 arrays

import numpy as np

x = np.array([1,2,3,4,5])
y = np.array([6,7,8,9,0])
z = np.add(x,y)
print(z)

# summation : adding all the values in 2 arrays

x = np.array([1,2,3,4,5])
y = np.array([6,7,8,9,0])
z = np.sum([x,y])
print(z)

# summation over an axis : if you specify axis = 1, numpy will sum the number in each array.

x = np.array([1,2,3,4,5])
y = np.array([6,7,8,9,0])
z = np.sum([x,y], axis=1)
print(z)

# cumulative sum : means partially adding elements in array
# example: [1,2,3,4] would be [1, 1+2, 1+2+3, 1+2+3+4]
# represented by cumsum()

x = np.array([1,2,3,4,5])
z = np.cumsum(x)
print(z)



