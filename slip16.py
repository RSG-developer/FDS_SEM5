# Write a python program to create two lists, one representing subject names and the other 
# representing marks obtained in those subjects. Display the data in a pie chart and bar chart. 
import pandas as pd
import matplotlib.pyplot as plt

subject =['JAVA','PHP','TCS','OS']
Marks=[30,28,25,20]
plt.figure(figsize=(10,6))
plt.subplot(221)
plt.pie(Marks,labels=subject,autopct='%0.1f%%')
plt.title("Marks Distribution of different Subjects")

plt.subplot(222)
plt.bar(subject,Marks,width=0.5,color=['green','red','blue','yellow'])
plt.title('Marks Distriibution')
plt.show()





#Write a python program to create a data frame for students’ information such as name, 
#graduation percentage and age. Display average age of students, average of graduation 
#percentage.

import pandas as pd

df=pd.DataFrame(columns=['Name','Age','percentage'])
df.loc[0]=['A',20,98]
df.loc[1]=['B',21,89]
df.loc[2]=['C',19,88]
df.loc[3]=['D',20,93]
df.loc[4]=['E',21,91]
print(df)
print(df.describe())
average_age=df['Age'].mean()
print("Average age of students is",average_age)
print("Average graduation percentage of students is",df['percentage'].mean())