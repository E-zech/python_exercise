# Get each digit from a number in the reverse order.
# For example, If the given integer number is 7536, 
# the output shall be “6 3 5 7“, with a space separating the digits.

def get_digit_rev():
    userInput = input("Enter a few digits number: ")
    userInput = userInput[::-1]

    for number in userInput:
        print(number, end=' ')
    print()

get_digit_rev()