# Delete a list of keys from a dictionary
# Expected output: {'city': 'New york', 'age': 25}

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

# Keys to remove
keys = ["name", "salary"]

for key in keys:
    sample_dict.pop(key)

print(sample_dict)