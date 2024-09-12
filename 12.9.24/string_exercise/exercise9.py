# Given a string s1, write a program to return the sum and average 
# of the digits that appear in the string, ignoring all other characters

str1 = "PYnative29@#8496"
sum = 0
count = 0

for num in str1:
    if num.isdigit():
        sum += int(num)
        count += 1

avg = sum / count
print(sum)
print(avg)