# we will make a copy , change in original array, and display both.

import numpy as np
x = np.array([1,2,3,4,5])
x1 = x.copy()
x1[0] = 42
print(x)
print(x1)

# make a view now

import numpy as np
x = np.array([1,2,3,4,5])
x1 = x.view()
x[0] = 42
print(x)
print(x1)


