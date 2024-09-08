# Display numbers from a list using a loop
# Write a Python program to display only those numbers from a list that satisfy the following conditions:

# The number must be divisible by five
# If the number is greater than 150, then skip it and move to the following number
# If the number is greater than 500, then stop the loop

numbers = [12, 75, 150, 180, 145, 525, 50]
sum_list = []

def calc_uniqe_choices(numbers):
    for num in numbers:
        if num > 500:
            break
        elif num % 5 == 0:
            if num > 150:
                continue
            else:
                sum_list.append(num)
    return sum_list 
    
print(calc_uniqe_choices(numbers))