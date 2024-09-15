# Write a program to determine which class a given Bus object belongs to.

class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass

school_bus = Bus("School Volvo", 12, 50)

if type(school_bus) == Vehicle:
    print('Born and raise a Vehicle class buddy')
else:
    print('My father was a Vehicle class but me is a Bus class')