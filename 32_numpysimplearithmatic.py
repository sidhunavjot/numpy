# arithmatic operators : +, - , / , *
# by using ufunc additional arguments like , where, dtype and out.
# here now we will use add()


import numpy as np
x = np.array([1,2,3,4,5])
y = np.array([6,7,8,9,0])
z = np.add(x,y)
print(z)


# substract

import numpy as np
x = np.array([1,2,3,4,5])
y = np.array([6,7,8,9,0])
z = np.subtract(x,y)
print(z)

# multiplication

import numpy as np
x = np.array([1,2,3,4,5])
y = np.array([6,7,8,9,0])
z = np.multiply(x,y)
print(z)


# devide

import numpy as np
x = np.array([1,2,3,4,5])
y = np.array([6,7,8,9,0])
z = np.divide(x,y)
print(z)

# power() function raises the value from the 1st array to the power of the values of the 2nd array and return the results in a new array

import numpy as np
x = np.array([1,2,3,4,5])
y = np.array([6,7,8,9,0])
z = np.power(x,y)
print(z)

# reminder - mode() and reminder() : these return reminder of the 1st array corresponding to 2nd array. Result comes in new array

import numpy as np
x = np.array([1,2,3,4,5])
y = np.array([6,7,8,9,0])
z = np.remainder(x,y)
print(z)

import numpy as np
x = np.array([1,2,3,4,5])
y = np.array([6,7,8,9,0])
z = np.mod(x,y)
print(z)

# Quotient and mode(remainder)
# the divmod() - this returns both quotient and mod.

import numpy as np
x = np.array([1,2,3,4,5])
y = np.array([6,7,8,9,0])
z = np.divmod(x,y)
print(z)

# absolute() and abs() - do the same function. but here we should use absolute() to avoid  confusion with python inbuilt function math.abs()

import numpy as np
x = np.array([1,2,3,4,5])
y = np.array([6,7,8,9,0])
z = np.absolute(x,y)
print(z)