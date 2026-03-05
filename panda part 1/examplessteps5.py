
"""

1- select specific column
2- filter rows
3- combine multiple condition


1-squre brackets
2- boolean condition 

selecting columns
1-a series
2- dataframe multiple columbs of data

column = df["Column Name]
subset =df["Column1","Column2"...]

filtering rows
boolean indexing


#based on a single condition
filtered_Rows = df[df["Salary"]>50000]

#combine multiple conditions
filter_Row = df[(df["Salary"]>50000) && (df["Age"]>30)



"""
import pandas as pd

data = {
    "Name": ['Ram', 'Shay', 'Ghanshyam', 'Dhanshyam', 'Aditi', 'Jagdish', 'Raj', 'Simram'],
    "Age": [28, 34, 30, 29, 40, 25, 32, 27],
    "Salary": [50000, 60000, 45000, 52000, 49000, 70000, 48000, 58000],
    "Performance Score": [85, 90, 78, 92, 88, 95, 80, 89]
}

df = pd.DataFrame(data)

print("Sample DataFrame")
print(df)

print("\nNames (Single column returns Series)")
name = df['Name']
print(name)

# selecting multiple columns
subset = df[["Name", "Salary"]]
print("\nSubset with Name and Salary")
print(subset)