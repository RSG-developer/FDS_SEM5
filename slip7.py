# Write a Python program to perform the following tasks : 
#a. Apply OneHot coding on Country column. 
#b. Apply Label encoding on purchased column 
#(Data.csv have two categorical column the country column, and the purchased column)

import pandas as pd
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
df=pd.read_csv('Data.csv')
print(df)
#df_encoded=pd.get_dummies(df,columns=['Country'],prefix=['Country'])
enc=OneHotEncoder(handle_unknown='ignore')
df_encoded=pd.DataFrame(enc.fit_transform(df[['Country']]).toarray())
print("One hot encoding\n ")
print(df_encoded)

label_encoder=LabelEncoder()
df['Purchased']=label_encoder.fit_transform(df['Purchased'])
print("Data with labelEncoding\n")
print(df)

