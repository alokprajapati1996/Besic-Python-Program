'''

@Author: Alok kumar

@Date: 24-11-23 6:00:30

@Last Modified by: Alok kumar

@Last Modified time: 24-11-2023 10:39:30

@Title : Besic-python-program

'''
sum=0
num=int(input("Enter a value: "))
if(num!=0):
    for i in range(1,num+1):
      sum=float(sum+1/i)
print(sum)