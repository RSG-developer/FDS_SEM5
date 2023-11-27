#Write a Python program to create box plots to see how each feature i.e. Sepal Length, 
#Sepal Width, Petal Length, Petal Width are distributed across the three species. (Use iris.csv 
#dataset)

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv('iris.csv')

plt.figure(figsize=(10,6))
plt.subplot(221)
plt.boxplot(df['sepal_length'],vert=False,patch_artist=True,boxprops=dict(facecolor='red'))
plt.title("sepal_length")
plt.subplot(222)
plt.boxplot(df['sepal_width'],vert=False,patch_artist=True,boxprops=dict(facecolor='orange'))
plt.title("sepal_width")
plt.subplot(223)
plt.boxplot(df['petal_length'],vert=False,patch_artist=True,boxprops=dict(facecolor='green'))
plt.title("petal_length")
plt.subplot(224)
plt.boxplot(df['petal_width'],vert=False,patch_artist=True,boxprops=dict(facecolor='blue'))
plt.title("petal_width")
plt.show()


# Use the heights and weights dataset and load the dataset from a given csv file into a 
#dataframe. Print the first, last 5 rows and random 10 row

df1=pd.read_csv('weight-height.csv')
print("First 5 rows are ",df1.head(5))
print("last 5 rows are ",df1.tail(5))
print("random 10 rows are ",df1.sample(10))