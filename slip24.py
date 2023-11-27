# Import dataset “iris.csv”. Write a Python program to create a Bar plot to get the 
#frequency of the three species of the Iris data. [10]
#  Q.2 B) Write a Python program to create a histogram of the three species of the Iris data.


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv('iris.csv')

species_count=df['species'].value_counts()
species_name=species_count.index
species_freq=species_count.values

plt.figure(figsize=(10,6))
plt.subplot(221)
plt.hist(species_name,bins=3,weights=species_count,width=0.5,align='mid')
plt.subplot(222)
sns.countplot(df['species'])

plt.show()