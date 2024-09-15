# Check if the first and last numbers of a list are the same

numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]

def check_f_l(my_list):
    first = my_list[0]
    last = my_list[::-1][0]
    return first == last



print(check_f_l(numbers_x)) # should be: True
print(check_f_l(numbers_y)) # should be: False