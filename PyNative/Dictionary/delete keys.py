# Exercise 6: Delete a list of keys from a dictionary
# Given:

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

# # Keys to remove
keys = ["name", "salary"]
# Expected output:

# {'city': 'New york', 'age': 25}

def list_of_keys(sample_dict, keys):
    my_dict = sample_dict.copy()
    for k , v in sample_dict.items():
        if k in keys:
            my_dict.pop(k)

    return my_dict

print(list_of_keys(sample_dict, keys))

def delete_keys(sample_dict,keys):
    for key in keys:
        sample_dict.pop(key, None)

    return sample_dict

print(delete_keys(sample_dict, keys))
            
