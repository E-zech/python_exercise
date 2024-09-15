# Sort JSON keys in and write them into a file
# Sort following JSON data alphabetical order of keys
import json

filePath = 'exercise4.txt'

sampleJson = {"id" : 1, "name" : "value2", "age" : 29}

with open(filePath, 'w') as file:
    json.dump(sampleJson, file, indent=4, sort_keys=True)

