# Create a recursive function
# Write a program to create a recursive function to calculate the sum of numbers from 0 to 10.
# A recursive function is a function that calls itself again and again.

num = 0

def calc(num):
    print(num)
    num += 1

    if num <= 10:
        calc(num)
    else:
        return (print('yep'))

calc(num)