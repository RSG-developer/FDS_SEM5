#Write a Python program to create a graph to find relationship between the petal length 
# and petal width.(Use iris.csv dataset)

import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv('iris.csv')
print(data)
petal_length=data['petal_length']
petal_width=data['petal_width']

plt.figure(figsize=(6,6))

plt.plot(petal_length,label='Petal_length',color='blue')
plt.plot(petal_width,label='Petal_width',color='red')
plt.title("petal_length vs petal_width ")
plt.legend()
plt.show()


# Write a Python program to find the maximum and minimum value of a given flattened 
# array. 

import numpy as np
arr=np.array([[1,2],[3,4]])
print(arr)
print("Minimum element is",np.min(arr))
print("Maximun element is ",np.max(arr))
