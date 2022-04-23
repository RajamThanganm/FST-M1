# fruits prices 
from re import search


fruits = {
         "apple":10, "banana":15, "cherries":25, "berries":27
         }

searchfruit = input("enter the name of the fruit to search for").lower()

if searchfruit in fruits:
   print(searchfruit)
else:
   print(" fruit not present")
