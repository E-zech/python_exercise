# Convert the following JSON into Vehicle Object
import json

json_dic = '{ "name": "Toyota Rav4", "engine": "2.5L", "price": 32000 }'

vehicle_dict = json.loads(json_dic)

class Vehicle:
    def __init__(self, name, engine, price):
        self.name = name
        self.engine = engine
        self.price = price


vehicleObj = Vehicle(**vehicle_dict)

print(vehicleObj.name)
print(vehicleObj.engine)
print(vehicleObj.price)