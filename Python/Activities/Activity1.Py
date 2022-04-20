userage = input("Enter your age")
username = input("Enter your name")
c= "user has entered name as " + username + " user has entered age as {}"
print(c.format(userage))

x=int(userage)
y=100-x

year = 2022 + y 
w= " The user will turn 100 years in {}"  
print(w.format(year))