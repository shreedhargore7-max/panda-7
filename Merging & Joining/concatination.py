"""
combining 2 data set verticaly and horizontaly

pd.concate([df1,df2],axis=0, ignore_index=True)

[df1,df2]=
axis = 1

ignore_index = True



"""

# verticaly

import pandas as pd

#region1

dfregion1 = pd.DataFrame({
  'CoustomerID':[1,2],
  'Name':['Ramesh','Shyam']

})

#region2

dfregion2 = pd.DataFrame({
  'CoustomerID':[3,4],
  'Name':['Suresh','Ghanshyam']

})

#conctenate verticaly

dfconcate = pd.concat([dfregion1,dfregion2], axis=1, ignore_index=True)

print(dfconcate)

