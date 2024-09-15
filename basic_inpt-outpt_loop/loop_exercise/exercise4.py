# Print multiplication table of a given number
def calc_multi():
    try:
        userInput = int(input("Enter a number between 1 - 10 : "))
        if userInput <= 0 or userInput > 10:
            print('please follow the instruction..')
            calc_multi()

        for num in range(1,11):
            print(userInput * num)

    except ValueError:
        return print(f'your input wasnt a number')

calc_multi()