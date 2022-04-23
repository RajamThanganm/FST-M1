"""
Tuple Number Checker

Activity 10

Given a tuple of numbers, iterate through it and print only those numbers which are divisible by 5
"""

Number_List = ((input("enter the numbers seperated by comma to find numbers divisible in the tuple").split(",")))
print(Number_List)

for number1 in Number_List:
    if int(number1)%5==0:
       print(number1)
    
       