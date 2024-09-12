# String characters balance Test
# Write a program to check if two strings are balanced. 
# For example, strings s1 and s2 are balanced if all the characters 
# in the s1 are present in s2. The character’s position doesn’t matter.

s1 = "Yn"
s2 = "PYnative"


for char in s1:
    if char not in s2:
        print(False)
    print(True)
    
