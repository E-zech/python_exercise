# Get an int value of base raises to the power of exponent
# Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.

def calc_exponent(base, exp):
    total = base **exp
    return total


base = 5
exponent = 4
print(calc_exponent(base, exponent))