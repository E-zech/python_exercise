# Initialize dictionary with default values

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

# Solution 1: update()
new_dict = {}

for employee in employees:
    new_dict.update({employee: defaults})

print(new_dict)


# Solution 2: fromkeys()
res = dict.fromkeys(employees, defaults)
print(res)