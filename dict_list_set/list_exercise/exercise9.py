# Replace list’s item with new value if found
# You have given a Python list. Write a program to find value 20 in the list, 
# and if it is present, replace it with 200. Only update the first occurrence of an item
# output: [5, 10, 15, 200, 25, 50, 20]

# Solution 1: 
list1 = [5, 10, 15, 20, 25, 50, 20]

num = list1.index(20)
list1.remove(20)
list1.insert(num,200)

print(list1)


# Solution 2: 
list2 = [5, 10, 15, 20, 25, 50, 20]

index = list2.index(20)
list2[index] == 200

print(list2)
