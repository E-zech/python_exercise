# Count all letters, digits, and special symbols from a given string
str1 = "P@#yn26at^&i5ve"

chars = 0
digits = 0
symbol = 0

for char in str1:

    if char.isalpha():
        chars += 1

    elif char.isdigit():
        digits += 1

    else:
        symbol += 1

print(f"Chars: {chars}\nDigits: {digits}\nSymbols: {symbol}")
