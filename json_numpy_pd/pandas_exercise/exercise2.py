# Clean the dataset and update the CSV file
# Replace all column values which contain ?, n.a, or NaN.

import pandas as pd 

filePath = 'exercise1.csv'
df = pd.read_csv(filePath)

newContent = df.replace(['?', 'n.a', pd.NA, None], 'Unknown')
newContent.to_csv(filePath, index=False)

