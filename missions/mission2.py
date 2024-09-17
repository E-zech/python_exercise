# extract from 'mission1.csv' the conent
# change the date format to: 01/01/2024 :'%d/%m/%Y %H:%M:%S'
# exract only the 16/09/2024 entries 
# save in new files while each file contain the same log level entreies

from datetime import datetime as dt
import re
import pandas as pd

file_path = 'mission1.csv'
specipec_date = dt(2024, 9, 16).strftime('%d/%m/%Y %H:%M:%S')

print(specipec_date)


df = pd.read_csv(file_path)
df['timestamp'] = pd.to_datetime(df['timestamp'], format='%Y-%m-%d %H:%M:%S').dt.strftime('%d/%m/%Y %H:%M:%S')
# print(df['timestamp'])


df_spec_time = [df['timestamp'] < specipec_date]
print(df_spec_time)