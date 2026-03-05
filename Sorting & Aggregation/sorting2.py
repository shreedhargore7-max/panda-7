
import pandas as pd

data = {
    "Name": ['Ram', 'Shay', 'Ghanshy'],
    "Age": [28, 34, 22],
    "Salary": [10000, 20000, 30000]
}

df = pd.DataFrame(data)

print("Before Sorting:")
print(df)

df.sort_values(by=["Age", "Salary"], ascending=False, inplace=True)

print("\nAfter Sorting:")
print(df)