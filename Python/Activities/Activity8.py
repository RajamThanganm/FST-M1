# Given a list of numbers, return True if first and last number of a list is same.
list1 = list(input("enter the numbers in the list seperated by a comma").split(","))
len_list = len(list1)
print(len_list)

if list1[0]==list1[len_list-1]:
   print("first and last item in the list are same")
else:
   print("first and last item in the list are not the same")