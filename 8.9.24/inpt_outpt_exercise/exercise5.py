# Accept a list of 5 float numbers as an input from the user

userInput = input('enter a list of 5 numbers seperated by space: ')

my_list = [float(num.strip()) for num in userInput.split()]

print(my_list)
