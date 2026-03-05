import pandas as pd

data = {
    "Name": ['Ram', None, 'Shay', 'Ghanshyam', 'Dhanshyam', 'Aditi', 'Jagdish', 'Raj', 'Simram'],
    "Age": [28, None, 34, 30, 29, 40, 25, 32, 27],
    "Salary": [50000, None, 60000, 45000, 52000, 49000, 70000, 48000, 58000],
    "Performance Score": [85, None, 90, 78, 92, 88, 95, 80, 89]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Fill missing values with appropriate values for each column
fill_values = {
    "Name": "Unknown",
    "Age": 0,
    "Salary": 0,
    "Performance Score": 0
}
df.fillna(fill_values, inplace=True)

print("\nUpdated DataFrame:")
print(df)

"""
10
20
30
40
50

1000


linear 
1-preserve data integrity
2- smooth trends
3- avoid data 


interpolate()

"""