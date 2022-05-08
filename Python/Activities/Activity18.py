import pandas as pd 
df = pd.read_csv("user_credentials.csv")
print(df)

print(df["Usernames"])   # Print the values only in the Usernames column
print(df["Usernames"][1] + " " + df["Passwords"][1])  # Print the username and password of the second row
print(df.sort_values("Usernames")) # Sort the Usernames column data in ascending order and print data
print(df.sort_values("Passwords", ascending=False)) # Sort the Passwords column in descending order and print data
