import pandas as pd
import numpy as np


data = pd.DataFrame([[1, 1.5],[0.5,2]], columns=['int', 'float'])
print(data.head())
#data.loc[data['int'] < 1.5, 'int'] = 0
# for i ,row in data.iterrows():
#     print(row['int'])
#     if row['int'] < 1.5:
#         print(data.loc[i,['int']])
#         data.loc[i,['int']] = np.nan

for index, row in data.iterrows():
    if row['int'] < 1:
        print(data.head(5))
        data.loc[index,['int']] = np.nan

print(data.head())
