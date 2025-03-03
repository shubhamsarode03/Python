
# Exercise 1: Convert two lists into a dictionary
# Below are the two lists. Write a Python program to convert them into a dictionary in a way that item from list1 is the key and item from list2 is the value

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
# Expected output:

# {'Ten': 10, 'Twenty': 20, 'Thirty': 30}

def convert_list(keys, values):
    my_dict = {}
    for index, key in enumerate(keys):
        my_dict[key] = values[index]
    return my_dict

print(convert_list(keys, values))


def convert_to_dict(keys, values):
    my_dict = {}
    for i in range(len(keys)):
        my_dict.update([(keys[i], values[i])]) or my_dict.update({keys[i]: values[i]})
    return my_dict

print(convert_to_dict(keys, values))


def convert_to_dictionary(keys, values):
    zip_tup = zip(keys, values)
    my_dict = dict(zip_tup)
    return my_dict

print(convert_to_dictionary(keys, values))