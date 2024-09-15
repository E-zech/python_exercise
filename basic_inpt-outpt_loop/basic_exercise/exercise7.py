# Find the number of occurrences of a substring in a string

str_x = "Emma is good developer. Emma is a writer"

def find_sub(string, sub_string):
    total = string.count(sub_string)
    return total 

print(find_sub(str_x, 'Emma'))