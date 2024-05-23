# Rayleigh dist : It is used in signal processing
# param - scale(standard deviation: default : 1.0), size

# sample for RL with scale 2.0 with size 2*3

from numpy import random
x = random.rayleigh(scale=2, size=(2,3))
print(x)

# visualization

from numpy import random
import seaborn as sns
import matplotlib.pyplot as plt

sns.displot(random.rayleigh(scale=2, size=1000))
plt.show()