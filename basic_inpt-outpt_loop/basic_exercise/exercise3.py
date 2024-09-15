# Write a Python code to accept a string from the user and display characters present at an even index number

def even_str ():
    user_Input = str(input('insert a word: '))
    length = len(user_Input)
    
# with %
    for i in range(length):
        if i % 2 == 0:
            print(f'{user_Input[i]}')

# witout %:
    # for i in range(0, length, 2):
    #     print(f'{user_Input[i]}')

even_str()    