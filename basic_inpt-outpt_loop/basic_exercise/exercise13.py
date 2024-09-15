# Print multiplication table from 1 to 10

def calc_multi_table():

    for x in range(1,11):
        for y in range(1,11):
            print(x * y, end=" ")
        print()

calc_multi_table()