# Exercise 3: Print the value of key ‘history’ from the below dict
sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
# Expected output:

# 80


def return_value(sampleDict):
    return sampleDict["class"]["student"]["marks"]["history"]


print(return_value(sampleDict))
