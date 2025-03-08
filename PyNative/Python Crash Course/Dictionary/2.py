# 6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers.
# Think of five names, and use them as keys in your dictionary. Think of a favorite 
# number for each person, and store each as a value in your dictionary. Print
# each person’s name and their favorite number. For even more fun, poll a few
# friends and get some actual data for your program

fav_numbers = {
    "Shubham": 3,
    "Saurav": 5,
    "Pratik": 24,
    "Vikas": 12,
    "Suraj": 20,

}

for k, v in fav_numbers.items():
    print(f"favourite number of {k} is {v}")


fav_dict ={}
number = len(fav_dict)
while number <= 5:
    name = input("whats your name?")
    fav_numbers = int(input(f"{name} please enter your fav number:" ))
    fav_dict[name] = fav_numbers

    number +=1


for k, v in fav_dict.items():
    print(f"favourite number of {k} is {v}")




