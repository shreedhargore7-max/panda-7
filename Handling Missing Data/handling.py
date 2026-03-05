"""

#dropna()

df.dropna(axis=1, inplce=true)


"""

import pandas as pd

data = {
    "Name": ['Ram',None, 'Shay', 'Ghanshyam', 'Dhanshyam', 'Aditi', 'Jagdish', 'Raj', 'Simram'],
    "Age": [28,None, 34, 30, 29, 40, 25, 32, 27],
    "Salary": [50000,None, 60000, 45000, 52000, 49000, 70000, 48000, 58000],
    "Performance Score": [85,None, 90, 78, 92, 88, 95, 80, 89]
}

df = pd.DataFrame(data)

df.dropna(axis=1,inplace=True)

print(df)