#Create a dataset data.csv having two categorical column (the country column, and the 
#purchased column). 
#a. Apply OneHot coding on Country column. 
#b. Apply Label encoding on purchased column 
import pandas as pd
from sklearn.preprocessing import OneHotEncoder,LabelEncoder

df=pd.read_csv('Data.csv')
print(df)

df_encoded=pd.get_dummies(df,columns=['Country'],prefix=['Country'])
print("One hot encoding is\n")
print(df_encoded)

label_Encoder=LabelEncoder()
df['Purchased']=label_Encoder.fit_transform(df['Purchased'])
print('Data with labelEncoder\n')
print(df)