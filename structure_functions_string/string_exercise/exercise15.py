#  Remove special symbols / punctuation from a string

str1 = "/*Jon is @developer & musician"
new_str = ''

for char in str1:
    if char.isalpha() or char.isspace():
        new_str += char

print(new_str)