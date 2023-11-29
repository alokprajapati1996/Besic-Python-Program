
"""
@Author: Alok kumar

@Date: 24-11-23 9:00:30

@Last Modified by: Alok kumar

@Last Modified time: 24-11-2023 9:00:30

@Title : tuple practice all the function

"""
tuple_1 = (1, 2, 3, 4, 5)
print(tuple_1)
print(len(tuple_1))
print(tuple_1[-3])
print(tuple_1[2:4])
print(tuple_1[:])

print(tuple_1[-5:-1])

# Check number exist or not
if 4 in tuple_1:
    print("yes exist")
# Check tuple length
print(type(tuple_1))

# access tuple

print(tuple_1[1])
# negative index
print(tuple_1[-1])

# range of item lik slicing
print(tuple_1[0:3])

# update tuple value
x = ("apple", "banana", "orange")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)
