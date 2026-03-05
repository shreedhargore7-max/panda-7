#adding columns

import pandas as pd

data = {
    "Name": ['Ram', 'Shay', 'Ghanshyam', 'Dhanshyam', 'Aditi', 'Jagdish', 'Raj', 'Simram'],
    "Age": [28, 34, 30, 29, 40, 25, 32, 27],
    "Salary": [50000, 60000, 45000, 52000, 49000, 70000, 48000, 58000],
    "Performance Score": [85, 90, 78, 92, 88, 95, 80, 89]
}

df = pd.DataFrame(data)

#squre bracket df["Column_Name"] = some_Data

df["Bonus"] = df['Salary']*0.1

print(df)

#using insert
#df.insert(loc,"Column_Name",some_data)

df.insert(0,"Emplyoe ID", [10,20,30,40,50,60,70,80])