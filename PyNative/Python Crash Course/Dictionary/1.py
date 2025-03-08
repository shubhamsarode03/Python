# 6-1. Person: Use a dictionary to store information about a person you know.
# Store their first name, last name, age, and the city in which they live. You
# should have keys such as first_name, last_name, age, and city. Print each piece
# of information stored in your dictionary

Person = {
    "first name": "Saurav",
    "last name": "Deshpande",
    "age": 25,
    "city": "Pune"
}

for k, v in Person.items():
    print(f"{k} is {v}")