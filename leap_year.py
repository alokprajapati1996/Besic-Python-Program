'''

@Author: Alok kumar

@Date: 27-11-23 8:00:30

@Last Modified by: Alok kumar

@Last Modified time: 24-11-2023 8:35:30

@Title : Besic-python-program

'''

year=int(input("Enter four digit year number: "))
if(year%400==0 )or (year%4==0 and year%100!=0):
    print("leap year")
else:
    print("not leap year")