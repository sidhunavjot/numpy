# data distribution is a list of all possible value and how often each value occur.

# such lists are important when working with statistics and data science

# Random distribution : Probability function

# Now we will generate 1-D with 100 values where eachvalue has to be 3,5,7,9

# the probability of value 3 is set to be 0.1
# the probability of value 5 is set to be 0.3
# the probability of value 7 is set to be 0.6
# the probability of value 9 is set to be 0
# sum of all probability numbers should be "1"

from numpy import random
x = random.choice([3,5,7,9], p=[0.1,0.3,0.6,0.0],size=(100))
print(x)


# Now we will return 2-D with 3 rows each containing 3 values

from numpy import random
x = random.choice([3,5,7,9], p=[0.1,0.3,0.6,0.0],size=(3,5))
print(x)

