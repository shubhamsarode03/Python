# Exercise 7: Check if a value exists in a dictionary
# We know how to check if the key exists in a dictionary. Sometimes it is required to check if the given value is present.

# Write a Python program to check if value 200 exists in the following dictionary.

# Given:

sample_dict = {'a': 100, 'b': 200, 'c': 300}
# Expected output:
target_value = 230
# 200 present in a dict

def check_value(sample_dict):
    for value in sample_dict.values():
        if value == 200:
            return True
        
print(check_value(sample_dict))

def check_value_exists(sample_dict, target_value):
    if target_value in sample_dict.values():
        return True
    else:
        return False
    
print(check_value_exists(sample_dict, target_value))