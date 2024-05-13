# splitting - it is reverse to joining

# array_split()

import numpy as np
x = np.array([1,2,3,4,5,6,7,8])
y = np.array_split(x,4)
print(y)

# split in 5

import numpy as np
x = np.array([1,2,3,4,5,6,7,8])
y = np.array_split(x,5)
print(y)

# split with 

import numpy as np
x = np.array([1,2,3,4,5,6,7,8])
y = np.array_split(x,3)
print(y[0])
print(y[1])
print(y[2])


# splitting with 2-D array

import numpy as np
x = np.array([[1,2],[3,4],[5,6],[7,8],[9,10],[11,12]])
y = np.array_split(x,3)
print(y)
print(y[0])
print(y[1])
print(y[2])

# split 2-D array into 3-D array

import numpy as np
x = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]])
y = np.array_split(x,3)
print(y)
print(y[0])
print(y[1])
print(y[2])

# splitting 2-d into three 2-d along with rows

import numpy as np
x = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]])
y = np.array_split(x,3, axis=1)
print(y) 


# alternate solution is using hsplit() , opposite of stack()

import numpy as np
x = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]])
y = np.hsplit(x,3)
print(y) 



