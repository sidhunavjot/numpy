# zipf dist: how many time a number/word will be occuring in a sentance,etc

# param - a(dist param), size

from numpy import random
x= random.zipf(a=2, size=(2,3))
print(x)

# visualization

from numpy import random
import seaborn as sns
import matplotlib.pyplot as plt

sns.displot(random.zipf(a=2, size=1000) )
plt.show()