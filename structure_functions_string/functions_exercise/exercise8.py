# Generate a Python list of all the even numbers between 4 to 30
# output: my_list = [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]

new_list = []
for num in range(4,30):

    if num % 2 == 0:
        new_list.append(num)

print(new_list)