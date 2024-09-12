# Create an inner function to calculate the addition in the following way
# Create an outer function that will accept two parameters, a and b
# Create an inner function inside an outer function that will calculate the addition of a and b
# At last, an outer function will add 5 into addition and return it


def calc_outer(a,b):

    def calc_inner(a,b):
        return a + b
    
    add5 = calc_inner(a,b)
    return add5 + 5

print(calc_outer(2,3))
        




