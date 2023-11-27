import pandas as pd
from sklearn.preprocessing import StandardScaler
df=pd.read_csv('winequality_red.csv')
scaler=StandardScaler()
standerize=pd.DataFrame(scaler.fit_transform(df),columns=df.columns)
print(standerize)