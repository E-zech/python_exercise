# Remove empty strings from the list of strings
# output :["Mike", "Emma", "Kelly", "Brad"]

list1 = ["Mike", "X", "Emma", "Kelly", "x", "Brad"]

res = list(filter(None, list1))

print(res)