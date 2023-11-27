#) Generate a random array of 50 integers and display them using a line chart, scatter plot. 
#Apply appropriate color, labels and styling options.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

random_data=np.random.randint(1,100,50)
print(random_data)

plt.figure(figsize=(10,6))
plt.subplot(221)
plt.plot(random_data,color='blue')
plt.title("Line plot")

plt.subplot(222)
plt.scatter(range(50),random_data,color='green')
plt.title('Scatter plot')

plt.subplot(223)
plt.hist(random_data,bins=10,color='red',edgecolor='black')
plt.title("histogram ")

plt.subplot(224)
plt.boxplot(random_data,vert=False,patch_artist=True,boxprops=dict(facecolor='red'))
#plt.show()



#Create two lists, one representing subject names and the other representing marks 
#obtained in those subjects. Display the data in a pie chart. 

subject=["Maths","English","History","Science"]
Marks=[90,80,87,88]
plt.pie(Marks,labels=subject,autopct='%1.1f%%',startangle=120)
#plt.show()


#) Write a program in python to perform following task (Use winequality-red.csv ) [5]
#Import Dataset and do the followings: 
# a) Describing the dataset 
# b) Shape of the dataset 
# c) Display first 3 rows from datase

df=pd.read_csv('winequality_red.csv')
print(df)
print("Describing the dataset \n",df.describe())
print("Shape of the dataset\n",df.shape)
print("first three rows are",df.head(3))

