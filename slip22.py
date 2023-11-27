import pandas as pd

df=pd.read_csv('winequality_red.csv')

from sklearn.preprocessing import MinMaxScaler
scaler=MinMaxScaler()
df_MinMaxScaler=pd.DataFrame(scaler.fit_transform(df),columns=df.columns)
print(df_MinMaxScaler)

from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
df_Scaled=pd.DataFrame(scaler.fit_transform(df),columns=df.columns)
print(df_Scaled)


from sklearn.preprocessing import Normalizer
normalizer=Normalizer()
df_normalizer=pd.DataFrame(normalizer.transform(df),columns=df.columns)
print(df_normalizer)