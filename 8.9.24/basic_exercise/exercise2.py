# Write a Python code to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number.

# loop 10 times
for number in range(10):
    # declare a variable equals to = {number} -1
    preNum = number -1
    # calc sum 
    sum = number + preNum

    # when number == 0 
    if number == 0:
        print(f'current number: {number}, prev number: {number}, sum: {number}')
    # when number not equals to 0 
    else:
        print(f'current number: {number}, prev number: {preNum}, sum: {sum}')