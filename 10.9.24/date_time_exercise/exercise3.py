from datetime import datetime, timedelta

# Subtract a week (7 days)  from a given date in Python
# output: 2020-02-18

given_date = datetime(2020, 2, 25)

new_date = given_date - timedelta(days=7)

print(new_date)