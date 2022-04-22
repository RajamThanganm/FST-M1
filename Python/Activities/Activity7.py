# sum of all numbers in a list 
list1 = list(input("Enter a sequence of comma separated values: ").split(","))
	
sum = 0
	
for list2 in list1:
	
  sum += int(list2)
	
print(sum)