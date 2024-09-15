# Create a recursive function
# Write a program to create a recursive function to calculate the sum of numbers from 0 to 5.
# A recursive function is a function that calls itself again and again.


def calc(num):

    if num:
        return num + calc(num - 1)

    else:
        return 0

print(calc(5)) # 15

# 1 round:
# calc(5):
#     return 5 + calc(5 - 1)   |   # return 15

# 2 round:
# calc(4):
#     return 4 + calc(4 - 1)   |   # return 10

# 3 round:
# calc(3):
#     return 3 + calc(3 - 1)   |   # return 6

# 4 round:
# calc(2):
#     return 2 + calc(2 - 1)   |   # return 3

# 5 round:
# calc(1):
#     return 1 + calc(1 - 1)   |   # return 1

# 6 round:
# calc(0):
#     return 0 + calc(0 - 1)   |   # return 0 

