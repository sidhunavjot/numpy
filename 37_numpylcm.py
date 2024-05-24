# finding LCM(Lowest common multiple)

# find lcm of 2 numbers

import numpy as np

x = 4
y = 6
z = np.lcm(x,y)
print(z)

# finding LCM in array

import numpy as np

x = np.array([3,6,9])
y = np.lcm.reduce(x)

# reduce() method will use the ufunc , in this case the lcm() function on each element and it will reduce the array by 1 dimension

print(y)

# find the LCM of an array where the array contains all integenrs from 1 - 10.

import numpy as np
x = np.arange(1,11)
y = np.lcm.reduce(x)
print(y)

 