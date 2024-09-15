# Check if a value exists in a dictionary
# We know how to check if the key exists in a dictionary. Sometimes it is required to check if the given value is present.

# Write a Python program to check if value 200 exists in the following dictionary.

sample_dict = {'a': 100, 'b': 200, 'c': 300}

# Solution 1(PYnative):
if 200 in sample_dict.values():
    print('200 present in a dict')

# Solution 2(me):
for value in sample_dict.values():
    if value == 200:
        print(f'{value} present in a dict')
