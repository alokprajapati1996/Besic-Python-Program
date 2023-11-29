"""

@Author: Alok kumar

@Date: 29-11-23 10:10:30

@Last Modified by: Alok kumar

@Last Modified time: 24-11-2023 10:54:30

@Title : Dictionary practice program

"""
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

# Duplicates not allowed

dict_1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 2020
}
print(dict_1)

# length
print(len(dict_1))
# type
print(type(dict_1))

# Creating an empty Dictionary
dict2 = {}
print("Empty Dictionary: ")
print(dict2)

# Creating a Dictionary
# with dict() method
dict2 = dict({1: 'Hcl', 2: 'WIPRO', 3: 'Facebook', 4: 'Bridgelabz'})
print("\nCreate Dictionary by using  dict(): ")
print(dict2)


