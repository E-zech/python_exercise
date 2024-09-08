# Write a Python code to remove characters from a string from 0 to n and return a new string.

def remove_chars(string, number):
    result = string[number:]
    print(result)

remove_chars("PYnative", 4)
remove_chars("PYnative", 2)