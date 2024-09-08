# Check Palindrome Number

def check_palindrome(number):
    rev_number = int(str(number)[::-1])
    return number == rev_number

num1 = 5445
num2 = 763

print(check_palindrome(num1))
print(check_palindrome(num2))