import pandas as pd

df1 = pd.read_csv('BlackCat.csv')
df2 = pd.read_csv('Departed.csv')
df3 = pd.read_csv('NoChoice.csv')
df4 = pd.read_csv('LoserMan.csv')
df5 = pd.read_csv('Facing_Mirrors.csv')
df6 = pd.read_csv('The_Late_Father.csv')
df7 = pd.read_csv('Death_of_Salesman.csv')



data = pd.concat([df1,df2,df3,df4,df5,df6,df7])

Total_data = pd.DataFrame(data)

Total_data.to_csv('./data.csv')