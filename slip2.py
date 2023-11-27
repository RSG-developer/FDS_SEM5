import pandas as pd

#question A
df=pd.read_csv('Data.csv')
#print(df)
df['Salary'].fillna(df['Salary'].mean(),inplace=True)
print(df)

df['Age'].fillna(df['Age'].mean(),inplace=True)
print(df)

#Question B
import matplotlib.pyplot as plt

df.plot(x='Country',y='Salary')
plt.show();

#quetsion C

data=pd.read_csv('weight-height.csv')
print("first 10 rows \n",data.head(10))
print("last 10 rows\n",data.tail(10))
print("random 20 rows\n",data.sample(20));