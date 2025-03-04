# Exercise 5: Create a dictionary by extracting the keys from a given dictionary
# Write a Python program to create a new dictionary by extracting the mentioned keys from the below dictionary.

# Given dictionary:

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# # Keys to extract
keys = ["name", "salary"]
# Expected output:

# {'name': 'Kelly', 'salary': 8000}

def create_dict(sample_dict, keys):
    my_dict = {}
    for k, v in sample_dict.items():
        if k in keys:
            my_dict[k] = v
    return my_dict

print(create_dict(sample_dict, keys))




