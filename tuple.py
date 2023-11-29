
"""
@Author: Alok kumar

@Date: 24-11-23 9:00:30

@Last Modified by: Alok kumar

@Last Modified time: 24-11-2023 9:00:30

@Title : tuple practice all the function

"""
tuple1=(1,2,3,4,5)
print(tuple1)
print(len(tuple1))
print(tuple1[-3])
print(tuple1[2:4])
print(tuple1[:])
print(tuple1[-5:-1])
#chek number exist or not
if 4 in tuple1:
    print("yes exist")
#check tuple length
print(type(tuple1))

#access tuple itam
print(tuple1[1])

#negative index
print(tuple1[-1])

#range of item lik slicing
print(tuple1[0:3])

#update tuple value
x = ("apple", "banana", "orange")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)
