#Generate a random array of 50 integers and display them using a line chart, scatter 
# plot, histogram and box plot. Apply appropriate color, labels and styling options

import numpy as np
import matplotlib.pyplot as plt

random_data=np.random.randint(1,100,50)

print(random_data)

plt.figure(figsize=(10,6))
plt.subplot(221)
plt.plot(random_data,color='blue')
plt.title("line chart")

plt.subplot(222)
plt.hist(random_data,label=10,color='red',edgecolor='black')
plt.title("histogram ")

plt.subplot(223)
plt.scatter(range(50),random_data,color='green')
plt.title("Scatter plot")

plt.subplot(224)
plt.boxplot(random_data,vert=False,patch_artist=True,boxprops=dict(facecolor='white'))
plt.show()


#Create two lists, one representing subject names and the other representing marks 
#obtained in those subjects. Display the data in a pie chart.

subjects=['Java','OS','PHP','TCS']
Marks=[90,89,78,88]

plt.pie(Marks,labels=subjects,autopct='%1.1f%%',startangle=120)
plt.show()
