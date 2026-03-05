#min max mean any sum
"""

df["Column Name"].sum()
df["Column Name"].mean()
df["Column Name"].min()
df["Column Name"].max()


""" 

import pandas as pd

data = {
    "Name": ['Ram', 'Shay', 'Ghanshy'],
    "Age": [28, 34, 22],
    "Salary": [10000, 20000, 30000]
}

df = pd.DataFrame(data)

avgsalary =df['Salary'].mean()
print(avgsalary)