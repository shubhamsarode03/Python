
# Exercise 8: Rename key of a dictionary
# Write a program to rename a key city to a location in the following dictionary.

# Given:

sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}
# Expected output:

# {'name': 'Kelly', 'age': 25, 'salary': 8000, 'location': 'New york'}

def rename_key(sample_dict):
    value = sample_dict.pop("city")
    sample_dict["location"] = value
    return sample_dict

print(rename_key(sample_dict))
