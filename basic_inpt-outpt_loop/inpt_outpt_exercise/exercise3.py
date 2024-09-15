# Convert Decimal number to octal using print() output formatting %o

def calc_octal():
    userInput = int(input('Enter any number: '))
    decimal_octal = f"{userInput:o}"
    return decimal_octal

print(calc_octal())
