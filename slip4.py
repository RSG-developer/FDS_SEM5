# Generate a random array of 50 integers and display them using a line chart, scatter 
#plot, histogram and box plot. Apply appropriate color, labels and styling options

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

random_data=np.random.randint(1,100,50)

print(random_data)

plt.figure(figsize=(12,6))
plt.subplot(221)
plt.plot(random_data,color='blue')
plt.title("line plot")
#plt.show()

plt.subplot(222)
plt.scatter(range(50),random_data,color='green')
plt.title("Scatter plot")
#plt.show()

plt.subplot(223)
plt.hist(random_data,bins=10,color='red',edgecolor='black')
plt.title('Histogram ')

plt.subplot(224)
plt.boxplot(random_data,vert=False,patch_artist=True,boxprops=dict(facecolor='red'))
plt.title('BOx plot')
plt.show()