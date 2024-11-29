#importing pandas
import pandas as pd
#importing matplotlib
import matplotlib.pyplot as plt
#reading dataframe
df=pd.read_csv("tt.csv")
#
#minimum and maximum values of ages
minage=df['Age'].min()
print("the minimum age is " ,minage)
#
maxage=df['Age'].max()
print("the maximum age is " ,maxage)
#creating bin
#
bins=[0,15,30,45,60,75]
df['binage']=pd.cut(df['Age'],bins)

age_labels=['Young','Young-Adult','Middle Aged','Middle Old Age','Senior']
df['binage']=pd.cut(df['Age'],bins,labels=age_labels)
print(df['binage'])
#creating a graph
df['binage'].value_counts().plot(kind='bar')
plt.title("AGE DISTRUBUTION")
plt.xlabel('ages')
plt.ylabel('count of people of their ages')
plt.show()