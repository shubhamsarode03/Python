# Exercise 9: Get the key of a minimum value from the following dictionary
sample_dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}
# Expected output:

# Math

def min_value_key(sample_dict):
     s =  min(sample_dict.values())
     for k , v in sample_dict.items():
          if s == v:
               return k


print(min_value_key(sample_dict))


