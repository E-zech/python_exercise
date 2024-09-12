#1A. Create a string made of the first, middle and last character

str1 = "Naruto"

length = len(str1)
mid_length =  int(length / 2)

first = str1[0]
middle = str1[mid_length]
last = str1[::-1][0]

# another wat to get last character
# last = str1[length - 1]


print(first + middle + last)


# 1B: Create a string made of the middle three characters
str1 = "JhonSasPeta"
str2 = "loraiukegrumg"
my_list = [str1, str2]
res = ''

for str in my_list:
    mid = int(len(str) / 2)
    res += str[mid - 1: mid + 2]

print(res)
