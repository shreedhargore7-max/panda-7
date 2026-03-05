import pandas as pd

data = {
    "Name": ['Ram', 'Shay', 'Ghanshy','Narun','Marun'],
    "Age": [28, 34, 22,49,15],
    "Salary": [10000, 20000, 30000,45000,50000]
}

df = pd.DataFrame(data)

grouped = df.groupby("Age")["Salary"].sum()

#grouped = df.groupby(["Age","Name"])["Salary"].sum() for mutiple columns

print(grouped)

"""
dr.groupby("Age")
age = 24 > [45000]
age = 28 [50000,48000]
age = 34 [60000,52000]

[Salary].sum()
age = 24 > [45000]
age = 28 [50000,48000] = 98000
age = 34 [60000,52000] = 110000






"""




"""
1- sum()
2- mean()
3- min()
4- max
5- count()
6- std()




"""