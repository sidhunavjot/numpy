# chisquare dist - it is used as a basis to verify hypothesis.

# params - df(degree of freedom), size

# sample for chi squared dist with df 2 with size 2*3

from numpy import random
x= random.chisquare(df=2, size=(2,3))
print(x)

# Visualization 

from numpy import random
import  seaborn as sns
import matplotlib.pyplot as plt

sns.displot(random.chisquare(df=2, size=1000))
plt.show()