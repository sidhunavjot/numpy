# uniform distribution - it is only made for probability(p)

# param - a (lower bound/value of probability. i.e : 0.0), b (upper bound/value of probability. i.e : 1.0), size

from numpy import random
x= random.uniform(size=(2,3))
print(x)

# visualization of uniform distribution

from numpy import random
import seaborn as sns
import matplotlib.pyplot as plt

sns.displot(random.uniform(size=(2,3)))
plt.show()