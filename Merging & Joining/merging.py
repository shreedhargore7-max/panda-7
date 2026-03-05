"""

pd.merge(df1,df2, on="Column_Name", how="type of join")

"""


import pandas as pd

dfcustomer = pd.DataFrame({
  'CoustomerID':[1,2,4],
  'Name':['Ramesh','Shyam','Ghanshyam']
})



dforder = pd.DataFrame({
  'OrderAmount':[101,102,103],
  'CoustomerID':[1,2,3]
})

dfmerged = pd.merge(dfcustomer,dforder, on="CoustomerID", how="inner")

dfmerged = pd.merge(dfcustomer,dforder, on="CoustomerID", how="outer")

dfmerged = pd.merge(dfcustomer,dforder, on="CoustomerID", how="left")

dfmerged = pd.merge(dfcustomer,dforder, on="CoustomerID", how="right")

print(dfmerged)

"""
1df = m rows
2df = n rows
m * n rows


"""