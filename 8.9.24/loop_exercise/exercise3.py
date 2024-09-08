# Calculate sum of all numbers from 1 to a given number:
# For example, if the user entered 10, the output should be 55 (1+2+3+4+5+6+7+8+9+10)

def calc():
    total = 0
    try:
        userInput = int(input("Enter a number to recive its sum: "))
        for n in range(1, userInput + 1, 1):
            total += n
            print(n, end="+")
        print(f'\nthe total is: {total}')

    except ValueError:
        print(f'your input wasnt an intger')
calc()