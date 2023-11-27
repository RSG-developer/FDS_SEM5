# Write a python program to Display column-wise mean, 
# and median for SOCR HeightWeight dataset

import pandas as pd

df=pd.read_csv('weight-height.csv')
print(df)
print(df.describe())
meanOF_height=df['Height'].mean()
medianOF_height=df['Height'].median()
print("mean of height column is ",meanOF_height)
print("median of height column is ",medianOF_height)


#Write a python program to compute sum of Manhattan distance between all pairs of 
#points.
def manhattan_distance(point1 ,point2 ):
    return abs(point1[0]-point2[0]) + abs(point1[1]-point2[1])

def sum_manhattan_distance(points):
    total_distance=0
    n=len(points)
    
    for i in range(n):
        for j in range(i+1,n):
            total_distance+=manhattan_distance(points[i],points[j])
    return total_distance

points=[(1,2),(3,5),(7,2)]
result=sum_manhattan_distance(points)
print(result)
