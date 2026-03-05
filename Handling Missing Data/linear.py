import pandas as pd

data = {
    "Time":[1,2,3,4,5],
    "Value":[10,None,20,None,30]
}

df = pd.DataFrame(data)

print("Before interpolation")
print(df)

df["Value"] = df["Value"].interpolate(method="linear")

print("After interpolation")
print(df)

"""
1- timer series data like stock market whare is data is changing for perticulaot time 

2-numeric data with trend || missing data in malls there we can use


3- avoide dropping rows




"""