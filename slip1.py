import pandas as pd
import matplotlib.pyplot as plt
# question A
#Write a Python program to create a Pie plot to get the frequency of the three species of 
#the Iris data (Use iris.csv)
df=pd.read_csv('iris.csv')
print(df)
species_count=df['species'].value_counts()
species_name=species_count.index
species_freq=species_count.values
plt.pie(species_freq,labels=species_name, autopct='%1.1f%%',startangle=120 )
plt.show()


#question B
data=pd.read_csv('winequality_red.csv')
print(data)
print(data.describe())