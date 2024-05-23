# Paretto dist : its a law of 80:20 ratio. where 20% is factor cause and 80%  is outcome.
# param - a(shape), size

# sample for pareto dist shape 2 and size 2*3

from numpy import random
x= random.pareto(a=2, size=(2,3))
print(x)

# visualization

from numpy import random
import seaborn as sns
import matplotlib.pyplot as plt

sns.displot(random.pareto(a=2, size=1000))
plt.show()
