# Permutation refers to an arrangment of elements like [3,2,1] is permutation of [1,2,3] and vice versa

# The numpy random module provides 2 methods : shuffle() and permutation()

# shuffle() method make changes to the original array
# Random shuffle

from numpy import random
import numpy as np

x = np.array([1,2,3,4,5])
random.shuffle(x)
print(x)

# permutation() doesn't work on original array, it works on copy array
# Permutation leaves original array as it is
# now generate permutaion of elements of array

from numpy import random
import numpy as np

x = np.array([1,2,3,4,5])

print(random.permutation(x))

