# Below are the two lists. Write a Python program to convert them into a dictionary in a way that item from list1 is the key and item from list2 is the value


# Solution 1: zip()
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

# zip/combine each key and value as a tuple(pair of key, vlaue), inside a list
zipped = zip(keys, values)

# when you pass this zip object to the dict() constructor, it converts the tuples into key-value pairs for the dictionary
my_dict = dict(zipped)

# in short:
# my_dict = dict(zip(keys,values))

print(my_dict)



# Solution 2: update()
low_keys = ['onw', 'Two', 'Three']
low_values = [1, 2, 3]

my_lower_dict = {}

# using i (as index) to iterate over the length of keys,
for i in range(len(low_keys)):

    # updates the dictionary with the specified key-value pairs
    # for each keys[i]:values[i]
    # means = for each key in keys, at index [i] (can be 0/1/2), 
    # will have the value at the same index position, values[i]
    my_lower_dict.update({keys[i]: low_values[i]})

print(my_lower_dict)