# PrettyPrint following JSON data
# PrettyPrint following JSON data with indent level 2 and key-value separators should be (",", " = ").
import json

sampleJson = {"key1": "value1", "key2": "value2", "key3": "value3"}

prett_please = json.dumps(sampleJson, indent=2, separators=(","," = "), sort_keys=False)

print(prett_please)


