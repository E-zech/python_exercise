# Create a Bus class that inherits from the Vehicle class. Give the capacity argument of Bus.seating_capacity() a default value of 50.

# Use the following code for your parent Vehicle class.

class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"
    

class Bus(Vehicle):

    # Override the original method from the Vehicle class
    def seating_capacity(self):

        # Declare a defualt 50 for capacity
        capacity = 50

        # Call the seating_capacity method from the parent class (Vehicle) with the default capacity of 50,
        # and return its result
        return super().seating_capacity(capacity)




new_bus = Bus('Volvo', 110, 630100)
print(new_bus.seating_capacity())