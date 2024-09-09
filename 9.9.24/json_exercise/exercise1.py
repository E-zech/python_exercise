# Convert the following dictionary into JSON format
import json

py_dict = {"key1" : "value1", "key2" : "value2"}

jsonData = json.dumps(py_dict)
print(f'this is a JSON: {jsonData}')