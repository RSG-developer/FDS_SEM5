#Dataset Name: winequality-red.csv [15]
# Write a program in python to perform following task 
#a. Rescaling: Normalised the dataset using MinMaxScaler class 
#b. Standardizing Data (transform them into a standard Gaussian distribution with a mean of 
#0 and a standard deviation of 1)
#c. Binarizing Data using we use the Binarizer class (Using a binary threshold, it is possible 
#to transform our data by marking the values above it 1 and those equal to or below it, 0)

import pandas as pd

df=pd.read_csv('winequality_red.csv');
print(df)


#question A 
from sklearn.preprocessing import MinMaxScaler
scaler=MinMaxScaler();
df_MinMaxScaler=pd.DataFrame(scaler.fit_transform(df),columns=df.columns);
print(df_MinMaxScaler)

#question B
from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
df_StandardScaler=pd.DataFrame(scaler.fit_transform(df),columns=df.columns)
print(df_StandardScaler)

#question C
from sklearn.preprocessing import Binarizer
threshold=9
binarizer=Binarizer(threshold=threshold)
df_binarizer=pd.DataFrame(binarizer.fit_transform(df),columns=df.columns)
print(df_binarizer)

