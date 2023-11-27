import numpy as np
import matplotlib.pyplot as plt

random_data=np.random.randint(1,100,50)
outliers=[150,160]
data=np.concatenate((random_data,outliers))


plt.boxplot(random_data,vert=False,patch_artist=True,boxprops=dict(facecolor='green'))
plt.title('boxplot without outliers')
plt.show()

plt.boxplot(data,vert=False,patch_artist=True,boxprops=dict(facecolor='orange'))
plt.title("box plot with outliers")
plt.show()