# Finding GCD (greatest common denominator), also known as HCF(highest common factor)

# we will find the hcf of below 2 numbers

import numpy as np
x = 6
y = 9

z = np.gcd(x,y)
print(z)

# finding gcd in an array

import numpy as np

x = np.array([3,6,9])
y = np.gcd.reduce(x)
print(y)