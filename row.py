# head() first 5 rows tail() last 10 rows



import pandas as pd

df = pd.read_csv("sales_data_sample.csv", encoding="latin1")

print("Display 10 rows of first")
print(df.head(10))

print("\nDisplay 10 rows of last")
print(df.tail(10))