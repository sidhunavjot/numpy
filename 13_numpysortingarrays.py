# sort() - the numpy ndarray object has a function which is called sort(), and this will sort a specified array

import numpy as np
x = np.array([1,5,1,10,4,2,9,6,5,22,5,4,4])
y = np.sort(x)
print(y)

# sort alphabetically

import numpy as np
x = np.array(['w','r','s','u'])
y = np.sort(x)
print(y)

# sort boolean

import numpy as np
x = np.array([True,False,False,True])
y = np.sort(x)
print(y)

# sort 2-D

import numpy as np
x = np.array([[3,4,2,5,6,1,2,3],[4,5,6,2,3,45,43,2]])
y = np.sort(x)
print(y)