# Exponential dist : it is used for describing the time till next event that is like failure or success

# Params - scale(inverse of rate(see lam poisson dist))

# Here we will draw a sample for exponential dist with 2.0 scale and 2*3 size.

from numpy import random
x = random.exponential(scale=2, size=(2,3))
print(x)

# visualization

from numpy import random
import seaborn as sns
import matplotlib.pyplot as plt

sns.displot(random.exponential(scale=50, size=1000))
plt.show()
