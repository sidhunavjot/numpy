# Binomial distribution - also know dicrete distribution
# Example - toss of coin can only have 2 outcomes haid or tail only

# param - n(number of trials), p(probability), size(shape-returned array)

# given 10 trial for a coin which will generate 10 data points:

from numpy import random

x = random.binomial(n=10, p=0.5, size= 10)
print(x)

# visualization of binomial

from numpy import random
import seaborn as sns
import matplotlib.pyplot as plt

sns.displot(random.binomial(n=10, p=0.5, size= 1000))
plt.show()

# difference between normal and binomial - Normal (Continuous) and Binomial (Discrete)
# use 500 data point for binomial and under 100 data point for normal dist.

from numpy import random
import seaborn as sns
import matplotlib.pyplot as plt

sns.displot(random.normal(loc=50, scale=5, size=1000),label='Normal')
sns.displot(random.normal(n=100, p=0.5, size=1000),label='Binomial')
plt.show()