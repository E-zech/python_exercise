# Check whether following json is valid or invalid.
import json

def validateJSON(jsonData):
    try :
        json.loads(jsonData)
    except ValueError as err:
        return False
    return True


InvalidJsonData = """{ "company":{ "employee":{ "name":"emma", "payble":{ "salary":7000 "bonus":800} } } }"""

isValid = validateJSON(InvalidJsonData)

print(isValid)

# needs a re-exercise on this one..