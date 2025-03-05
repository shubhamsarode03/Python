# Exercise 4: Initialize dictionary with default values
# In Python, we can initialize the keys with the same values.

# Given:

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
# Expected output:

# {'Kelly': {'designation': 'Developer', 'salary': 8000}, 'Emma': {'designation': 'Developer', 'salary': 8000}}

def initialize_dict_by_default(employees, defaults):
    my_dict = {}
    for el in employees:
        my_dict[el] = defaults
    return my_dict

print(initialize_dict_by_default(employees, defaults))


def initialize_dict(employees, defaults):
    my_dict = {}
    for el in employees:
        my_dict.setdefault(el, defaults)
    return my_dict

print(initialize_dict(employees, defaults))


#When to Use fromkeys()?
# ✔ When you need a dictionary with default values quickly.
# ✔ Useful for initializing keys before assigning values.

def ini_dict(employees, defaults):
    my_dict = dict.fromkeys(employees, defaults)
    return my_dict
print(ini_dict(employees, defaults))

