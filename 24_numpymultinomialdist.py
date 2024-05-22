# Multinomial dist : It is generalization of binomial dist.

# params - n (number of outcomes), pvals(list of possibilities or outcomes, ex: 1-6 in dice rolls), size (shape of returned array)

# draw out a sample for dice roll

from numpy import random

x = random.multinomial(n=6, pvals=[1/6,1/6,1/6,1/6,1/6,1/6], size=10)
print(x)

# multinomial samples will not produce a single value. They will produce one value for each pvals

# Visualization normally not done here

