# Append new string in the middle of a given string
# Given two strings, s1 and s2. Write a program to create a new string s3 by appending s2 in the middle of s1.

s1 = "Ault"
s2 = "Kelly"

length = len(s1)
mid_len1 = int(length / 2)

s1_f = s1[:mid_len1] 
s1_l = s1[mid_len1:] 

print(s1_f + s2 + s1_l) 