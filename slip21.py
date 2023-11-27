#A) Import dataset “iris.csv”. Write a Python program to create a Bar plot to get the 
# frequency of the three species of the Iris data. 
# B)Write a Python program to create a histogram of the three species of the Iris data



import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('iris.csv')
spiecies_count=df['species'].value_counts()
species_name=spiecies_count.index
spiecies_counts=spiecies_count.values

plt.bar(species_name,spiecies_counts,color=['b','g','r'])
plt.show()

plt.hist(species_name,bins=3,weights=spiecies_counts,align='mid',rwidth=0.8)
plt.show()
