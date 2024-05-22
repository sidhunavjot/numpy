# poisson dist - also a discrete dist. 
# Tells how many times that event will occur

# params - lam(number of occurances or rate), size

# generate a random 1*10 dist for the occurance 2

from numpy import random

x = random.poisson(lam=2, size=10)
print(x)

# visualization of poisson plot

from numpy import random
import seaborn as sns
import matplotlib.pyplot as plt


sns.displot(random.poisson(lam=50, size=1000))
plt.show()

 

