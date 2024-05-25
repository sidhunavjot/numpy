# Trignomentry func : numpy provides the ufuncs like sin(), cos() and tan() that takes value in radians and produce other values in tan, cos and sin

# find the sin() value of pi/2

import numpy as np
x = np.sin(np.pi/2)
print(x)

# find in arrays

import numpy as np
x = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/6])
y = np.sin(x)
print(y)

