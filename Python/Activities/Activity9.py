# Given a two list of numbers create a new list such that new list should contain only odd numbers 
# from the first list and even numbers from the second list

listone = [1,2,3,4,5,6,7,8,9,10]
listtwo = [11,12,13,14,15,16,17,18,19,20]

listthree=[]
for i in listone:
    if i%2!=0:
       listthree.append(i)

for j in listtwo:
    if j%2==0:
       listthree.append(j)

print(listthree) 