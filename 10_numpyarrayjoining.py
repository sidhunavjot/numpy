# Joining the numpy array - here for this we will pass concatenate

import  numpy as np
x = np.array([1,2,3])
y = np.array([4,5,6])
z = np.concatenate((x,y))
print(z)

# Joining of 2-D arrays along with rows(axis = 1)

import  numpy as np
x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])
z = np.concatenate((x,y), axis=1)
print(z)

# joining array using the stack function

import  numpy as np
x = np.array([1,2,3])
y = np.array([4,5,6])
z = np.stack((x,y), axis=1)
print(z)


# Stacking along with rows : hstack()

import  numpy as np
x = np.array([1,2,3])
y = np.array([4,5,6])
z = np.hstack((x,y))
print(z)

# Stacking along with columns : vstack()

import  numpy as np
x = np.array([1,2,3])
y = np.array([4,5,6])
z = np.vstack((x,y))
print(z)

# Stacking along with height : dstack()

import  numpy as np
x = np.array([1,2,3])
y = np.array([4,5,6])
z = np.dstack((x,y))
print(z)



