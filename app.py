import pandas as pd


#read data from CSV file into a dataframe

#df = pd.read_csv("sales_data_sample.csv", encoding="latin1")


#read data from excell file into a dataframe

#df = pd.read_json("sample_Data.json", encoding="latin1")


#read data from excell file into a dataframe

df = pd.read_excel("SampleSuperstore.xlsx", encoding="latin1")

#gcsfs to take data from clude   have to use this library read


print(df)