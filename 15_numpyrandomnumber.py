# random meaning : something that can not be logically predicted

# Now we will generate a random number

from numpy import random
x = random.randint(1000)
print(x)

# you can also generate float() via rand()

from numpy import random
x = random.rand()
print(x)

# you can also generate random array

# we will generate a 1-D array containing 5 random int from 0 to 100

from numpy import random
x = random.randint(1000, size=(1000))
print(x)
 

# we will create 2-D array with 3 rows , each row containing 5 random int 0 to 100

from numpy import random
x = random.randint(1000, size=(3,5))
print(x)

# creat float value array

from numpy import random
x = random.rand(3,5)
print(x)


# you can also generate random numbers from an array 
# choice()

from numpy import random
x = random.choice([3,4,2,1,55,6,67,88,6,5])
print(x)


