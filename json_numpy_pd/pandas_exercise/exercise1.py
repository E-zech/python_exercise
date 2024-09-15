# From the given dataset print the first and last five rows

import pandas as pd 

filePath = 'exercise1.csv'
df = pd.read_csv(filePath)

print(df.head(5))
print(df.tail(5))
