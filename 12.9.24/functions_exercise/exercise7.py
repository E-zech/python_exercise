# Assign a different name to function and call it through the new name
# Below is the function display_student(name, age). 
# Assign a new name show_student(name, age) to it and call it using the new name

name = 'Gohan'
age = 35

def display_student(name, age):
    print(name, age)

show_student = display_student

show_student(name, age)