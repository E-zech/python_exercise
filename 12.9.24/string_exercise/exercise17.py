# Find words with both alphabets and numbers

str1 = "Emma25 is Data scientist50 and AI Expert"

new_list = str1.split()

for item in new_list:
    if any(char.isalpha() for char in item) and any(char.isdigit() for char in item):
        print(item)

