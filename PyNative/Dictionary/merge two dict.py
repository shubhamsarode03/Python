
# Exercise 2: Merge two Python dictionaries into one
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
# Expected output:

# {'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

def merge_dict(dict1, dict2):
    dict1.update(dict2) # modifying first dictionary thats why assignement is not possible
    return dict1


print(merge_dict(dict1, dict2))

#dict unpacking

def merger_dict(dict1,dict2):
    return {**dict1, **dict2}
    


print(merge_dict(dict1, dict2))