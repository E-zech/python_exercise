# Create a child class Bus that will inherit all of the variables and methods of the Vehicle class

class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass


new_bus = Bus('Volvo', 180, 12)

print(f'Vehicle Name: {new_bus.name}, Speed: {new_bus.max_speed}, Mileage: {new_bus.mileage}.')