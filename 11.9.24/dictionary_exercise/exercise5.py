# Create a dictionary by extracting the keys from a given dictionary
# Write a Python program to create a new dictionary by extracting the mentioned keys from the below dictionary.

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]

# for each key in keys, the value will be sample_dict[key], 
# means search for the key inside the sample_dict that its name == name of the ket form keys
my_dict = {key: sample_dict[key] for key in keys}
print(my_dict)

# another exercise
numbers_dict = {
    "a": 10,
    "b": 15,
    "c": 20,
    "d": 25
}

# iterates over key-value pair in numbers_dict using the items() method, 
# check if its even, then save as the new dict
filtered = {key: value for key, value in numbers_dict.items() if value % 2 == 0}

print(filtered)