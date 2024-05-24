# products : use prod() function

# here we will find the product of the element of the below array:


import numpy as np
x = np.array([1,2,3,4]) # 1*2*3*4 = 24
y = np.prod(x)
print(y)


# Here we will find the products of elements in 2 different array:

import numpy as np
x = np.array([1,2,3,4]) 
y = np.array([6,7,8,9])
z = np.prod([x,y]) # 1*2*3*4*5*6*7*8*9 = 24
print(z)

# product over an axis

import numpy as np
x = np.array([1,2,3,4]) 
y = np.array([6,7,8,9])
z = np.prod([x,y], axis=1) # 1*2*3*4 = 24 ........... 5*6*7*8*9 = 3024
print(z)

# cummulative product :
# example of partial product [1,2,3,4] is [1, 1*2, 1*2*3, 1*2*3*4 ]

import numpy as np
x = np.array([1,2,3,4]) 
z = np.cumprod([x,y])
print(z)