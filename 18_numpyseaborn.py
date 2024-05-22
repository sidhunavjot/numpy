# matplotlib ke andar pyplot hota hai uska use seaborn krta hai
# matplot(pyplot) - seaborn

# seaborn is alibrary that uses matplotin underneath to plot graph i.r pyplot.

# Distplot - distribution plot (curve plot - histogram)

import matplotlib.pyplot as plt
import seaborn as sns
sns.displot([0,1,2,3,4,5])
plt.show()

# plotting a displot without the histogram

import matplotlib.pyplot as plt
import seaborn as sns
sns.displot([0,1,2,3,4,5], hist = False)
plt.show()



   