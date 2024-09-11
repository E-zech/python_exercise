# Convert string into a datetime object

# given : "Feb 25 2020 4:20PM"
# output: 2020-02-25 16:20:00

from datetime import datetime


date_string = "Feb 25 2020 4:20PM"

timeObg = datetime.strptime(date_string, "%b %d %Y %I:%M%p").strftime("%Y-%m-%d %H:%M:%S")

print(timeObg)


