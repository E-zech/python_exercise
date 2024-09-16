from datetime import datetime as dt
# https://www.w3resource.com/python-exercises/date-time-exercise/
# Write a Python script to display the various Date Time formats :
# a) Current date and time
# b) Current year
# c) Month of year
# d) Week number of the year
# e) Weekday of the week
# f) Day of year
# g) Day of the month
# h) Day of week


# a) Current date and time
now = dt.now()
print(now)

# b) Current year
print(now.year)

# c) Month of year
print(now.month)

# d) Week number of the year
d = now.strftime('%W')
print(d)

# e) Weekday of the week
e = now.strftime('%w')
print(e)

# f) Day of year
f = now.strftime('%j')
print(f)

# g) Day of the month
g = now.strftime('%d')
print(g)

# h) Day of week
h = now.strftime('%A')
print(h)


