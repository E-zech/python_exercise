# Create a new string made of the first, middle, and last characters of each input string
# Given two strings, s1 and s2, 
# write a program to return a new string made of s1 and s2’s first, middle, and last characters

s1 = "America"
s2 = "Japan"

# Solution 1:
s1_len = len(s1)
s2_len = len(s2)

s1_mid = s1_len // 2
s2_mid = s2_len // 2

# first
s1_f = s1[0]
s2_f = s2[0]

# last
s1_l = s1[s1_len - 1]
s2_l = s2[s2_len - 1]

#mid
s1_mid = s1[s1_mid] 
s2_mid = s2[s2_mid] 

print(s1_f + s2_f + s1_mid + s2_mid + s1_l + s2_l)


# Solution 2:
my_list = [s1,s2]

first = ''
middle = ''
last = ''

for str in my_list:
    first += str[0]
    last += str[-1]
    middle += str[len(str) // 2]

print(first + middle + last)
