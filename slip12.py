# Write a Python program to create data frame containing column name, salary, department 
# add 10 rows with some missing and duplicate values to the data frame. Also drop all null and 
# empty values. Print the modified data frame

import pandas as pd

df=pd.DataFrame(columns=['Name','Salary','Department'])
df.loc[0]=['A',12000,'Sales']
df.loc[1]=['B',30000,'Marketing']
df.loc[2]=['C',10000,'Accounts']
df.loc[3]=['A', 12000,'Sales']
print(df)
print(df.duplicated())
