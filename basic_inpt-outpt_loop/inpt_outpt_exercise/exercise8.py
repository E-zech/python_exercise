# Write a program to use string.format() method to format the following three variables as per the expected output
# totalMoney = 1000
# quantity = 3
# price = 450
# I have 1000 dollars so I can buy 3 football for 450.00 dollars.


totalMoney = 1000
quantity = 3
price = 450

print(f'I have {totalMoney} dollars so i can buy {quantity} football for {float(price):.2f} dollars.')