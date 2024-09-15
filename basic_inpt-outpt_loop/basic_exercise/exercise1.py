# Given two integer numbers, write a Python code to return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.

num1 = 30
num2 = 500

def calc_sum_nulti(num1, num2):
    # calc multi
    multi = num1 * num2
    # calc sum
    sum = num1 + num2

    # if multi lower or equal to 1000 return multi, otherwise return sum
    if multi <= 1000:
        return multi
    else:
        return sum

print(calc_sum_nulti(num1, num2))