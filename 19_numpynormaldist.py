# Normal Distribution - Gaussian Distribution - Very Important

# random.normal() method - loc(mean), scale(standard deviation), size
# we are generating a random normal distribution of size 2*3

from numpy import random
x = random.normal(size=(2,3))
print(x)

# here we will generate a random normal dist of size 2*3 with mean at 1 and standard deviation of 2

from numpy import random
x = random.normal(loc=1, scale=2 ,size=(2,3))
print(x)


# visualization of normal distribution

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(random.normal(size=1000))
plt.show()

# the curve of a normal dist is also called as bell curve

