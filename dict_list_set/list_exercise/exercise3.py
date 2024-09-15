# Turn every item of a list into its square
# Given a list of numbers. write a program to turn every item of a list into its square.

numbers = [1, 2, 3, 4, 5, 6, 7]

# Solution 1:
res = []

for num in numbers:
    num = num ** 2
    res.append(num)

print(res)


# Solution 2: 
result = [num * num for num in numbers]

print(result)