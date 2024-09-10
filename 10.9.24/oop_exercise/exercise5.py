# Define a property that must have the same value for every class instance (object)
# Define a class attribute ”color” with a default value white. I.e., Every Vehicle should be white


class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.color = 'White'

        print(f'Color: {self.color}, Vehicle name: {self.name}, Speed: {self.max_speed}, Mileage: {self.mileage}')

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass



new_bus = Bus('School Volvo', 180, 120)
new_car = Car('Audi Q5', 260, 18)