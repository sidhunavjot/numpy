# logistic distribution - this descibes the growth. 
# very important in regression and neural network

# params - loc(mean- default value =0), scale(standard deviation, default value = 1), size

# draw 2*2 sample of logistics with mean at 1 and standard deviation at 2.

from numpy import random

x = random.logistic(loc=1, scale=2, size=(2,3))
print(x)

# Visualization of logistics

from numpy import random
import seaborn as sns
import matplotlib.pyplot as plt

sns.displot(random.logistic(loc=50, scale=2, size=1000))
plt.show()

