userage = input("Enter your age")
username = input("Enter your name")
c= "user has entered name as " + username + " user has entered age as {}"
print(c.format(userage))

x=int(userage)
y=100-x

w= " The user will turn 100 years in  {} years"
print(w.format(y))