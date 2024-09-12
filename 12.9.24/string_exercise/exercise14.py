# Remove empty strings from a list of strings

str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
new_list = list(filter(None, str_list))
print(new_list)
