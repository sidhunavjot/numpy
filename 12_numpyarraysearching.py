# searching arrays : you can search an array for a certain value and return the indexes that get the match

# by using where()

import numpy as np
x = np.array([1,2,3,4,5,4,4])
y = np.where(x==4)
print(y)

# find indexes where values are even

import numpy as np
x = np.array([1,2,3,4,5,4,4])
y = np.where(x%2==0)
print(y)

# find indexes where values are odd

import numpy as np
x = np.array([1,2,3,4,5,4,4])
y = np.where(x%2==1)
print(y)


# searchsorted()  -  it performs binary search in array

# we will now find the index where the value 7 should be inserted

import numpy as np
x = np.array([1,2,3,4,5,4,4])
y = np.searchsorted(x,2)
print(y)

# search from right side

import numpy as np
x = np.array([1,2,3,4,5,4,4])
y = np.searchsorted(x,2, side='right')
print(y)

# search multiple values
# where can we add these values ?

import numpy as np
x = np.array([1,2,3,4,5,4,4])
y = np.searchsorted(x,[2,4,6])
print(y)


