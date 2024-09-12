# Return multiple values from a function
# Write a program to create function calculation() such that 
# it can accept two variables and calculate addition and subtraction. 
# Also, it must return both addition and subtraction in a single return call.

def calc(a,b):
    substruction = a - b
    addition = a + b
    return print(f'substruction: {substruction}\naddition: {addition}')

calc(40,10)