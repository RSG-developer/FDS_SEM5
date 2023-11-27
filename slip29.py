import pandas as pd
from sklearn.preprocessing import OneHotEncoder,LabelEncoder
df=pd.read_csv('Data.csv')
print(df)

df_encoded=pd.get_dummies(df,columns=['Country'],prefix=['Country'])
print(df_encoded)


label_encoder=LabelEncoder();
df['Purchased']=label_encoder.fit_transform(df['Purchased']);
print(df)