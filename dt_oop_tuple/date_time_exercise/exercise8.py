# Write a Python program to determine whether a given year is a leap year.

def is_leap_year(year):
    def check_leap(year):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    
    if isinstance(year, list):
        return [f'{y} is a leap year' if check_leap(y) else f'{y} is not a leap year' for y in year]
    else:
        return f'{year} is a leap year' if check_leap(year) else f'{year} is not a leap year'



years = [2023, 2024, 2025]
print(is_leap_year(years))

year = 2024
print(is_leap_year(year))
    