# Convert the following Vehicle Object into JSON
import json
from json import JSONEncoder
from typing import Any

class Vehicle:
    def __init__(self, name, engine, price):
        self.name = name
        self.engine = engine
        self.price = price

class VehicleEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Vehicle):
            return {
                'name': obj.name,
                'engine': obj.engine,
                'price': obj.price
            }
        return super().default(obj)
    
        # another simple, less controlled and may include unwanted attributes or metadata which might not be suitable for all use cases:
        # return obj.__dict__
    
    

vehicle = Vehicle("Toyota Rav4", "2.5L", 32000)

vehicle_json = json.dumps(vehicle, cls=VehicleEncoder, indent=4)

print(vehicle_json)