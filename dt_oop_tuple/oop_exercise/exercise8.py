# Determine if School_bus is also an instance of the Vehicle class
class DiffrentClassNameForCheckingIfItIsADiffrentClassInstance:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus():
    pass

school_bus = DiffrentClassNameForCheckingIfItIsADiffrentClassInstance("School Volvo", 12, 50)

if isinstance(school_bus, Vehicle):
    print('Born and raise a Vehicle class buddy')
else:
    print('me no instance of Vehicle or Bus, me not belong here')