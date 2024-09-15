# Access the value of key2 from the following JSON
import json

sampleJson = """{"key1": "value1", "key2": "value2"}"""

py_dict = json.loads(sampleJson)

print(py_dict["key2"])
