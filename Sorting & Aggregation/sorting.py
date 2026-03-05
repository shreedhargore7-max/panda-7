#sorting data
#SORTING DATA: 1 COLUMN sort_value()
#df.sort_values(by="Column Name", TRUE/FALSE, inplace=true)



import pandas as pd

data = {
    "Name": ['Ram', 'Shay', 'Ghanshy'],
    "Age": [28, 34, 22],
    "Salary": [10000, 20000, 30000]
}

df = pd.DataFrame(data)

print("Before Sorting:")
print(df)

df.sort_values(by="Age", ascending=False, inplace=True)

print("\nAfter Sorting:")
print(df)