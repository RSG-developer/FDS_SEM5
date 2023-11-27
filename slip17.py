# Write a Python program to draw scatter plots to 
# compare two features of the iris dataset


import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv('iris.csv')
print(df.head(10))

petal_length=df['petal_length']
petal_width=df['petal_width']
sepal_len=df['sepal_length']
sepal_width=df['sepal_width']
plt.figure(figsize=(10,6))
plt.subplot(221)
plt.scatter(petal_length,petal_width,color='blue',marker='o')
plt.title('petallength vs petalwidth')

plt.subplot(222)
plt.scatter(sepal_len,sepal_width,color='green')
plt.title('sepal_length vs sepal_width')
plt.show()



#Write a Python program to create a data frame containing columns name, age , salary, 
# department . Add 10 rows to the data frame. View the data frame.
df=pd.DataFrame(columns=['Name','Age','Salary','department'])
df.loc[0]=['A',25,40000,'Xyz']
df.loc[1]=['B',23,30000,'abc']
df.loc[2]=['C',24,20000,'shh']
df.loc[3]=['D',26,23000,'sddssd']
print(df)