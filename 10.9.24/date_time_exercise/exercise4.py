# Print a date in a the following format
# Day_name  Day_number  Month_name  Year
# output: Tuesday 25 February 2020

from datetime import datetime

given_date = datetime(2020, 2, 25)

new_date_format = datetime.strftime(given_date, "%A %d %B %Y")
print(new_date_format)