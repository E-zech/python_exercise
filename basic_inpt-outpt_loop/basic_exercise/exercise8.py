# Print the following pattern :
# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5

# run 5 times
for num in range(1,6):
    # run {num} times
    for i in range(num):
        # print num, and instead of \n (newline), that is the default of print, use space as ' ' = end=' '.
        print(num, end=" ")
    # pprint a new line when the inner loop is finished
    print()
