# Removal all characters from a string except integers
str1 = 'I am 25 years and 10 months old'
new_str = ''

for char in str1:
    if char.isdigit():
        new_str += char

print(new_str)
