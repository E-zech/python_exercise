# Remove all occurrences of a specific item from a list.
# Given a Python list, write a program to remove all occurrences of item 20.

# Solution 1:

def remove_20(list, num):
    return [n for n in list if n != num]


list1 = [5, 20, 15, 20, 25, 50, 20]
num = 20
print(remove_20(list1, num))


# Solution 2:
list2 = [5, 20, 15, 20, 25, 50, 20]

how_many = list2.count(20)

for i in range(how_many):
    list2.remove(20)

print(list2)