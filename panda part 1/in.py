#1-columns, rows?
#2- what type of?
#3-missing data?


#info()

#1-number of row and columb\
#2- coluumn name
#3- in64 float64 object
#4- non null counts
#5- memory usage of the data frame



import pandas as pd

df = pd.read_csv("sales_data_sample.csv", encoding="latin1")


print('Displaying the info of data set')
print(df.info())