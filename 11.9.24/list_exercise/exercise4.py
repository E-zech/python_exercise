# Concatenate two lists in the following order:
# output: ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

new_list = [x + y for x in list1 for y in list2]
print(new_list)

