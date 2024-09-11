# Rename key of a dictionary
# Write a program to rename a key city to a location in the following dictionary.

sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}

if "city" in sample_dict.keys():
    ###### the new key name = the value of the old key name that has been deleted
    # when u use pop("city") its removes the key "city" from the dict and returns its value, which is "New york"
    sample_dict["location"] = sample_dict.pop("city")

print(sample_dict)