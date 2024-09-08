# Merge two lists using the following condition:

# Given two lists of numbers, write a Python code to create a new list such that the latest list should contain odd numbers from the first list and even numbers from the second list.

list1 = [10, 20, 25, 30, 35] # take odd numbers
list2 = [40, 45, 60, 75, 90] # take even numbers


def create_1_list(list1, list2):
    newList = []

    for num in list1:
        if num % 2 != 0:
            newList.append(num)

    for num in list2:
        if num % 2 ==0:
            newList.append(num)

    return newList

print(create_1_list(list1, list2))