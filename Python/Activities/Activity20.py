"""  Print the number of rows and columns
    Print the data in the emails column only
    Sort the data based on FirstName in ascending order and print the data"""
import pandas as pd
from pandas import ExcelFile
from pandas import ExcelWriter

DF = pd.read_excel("C:\\Users\\RAJAMTHANGAM\\Activity19_empdetails.xlsx", sheet_name='Sheet1')

# Print the number of rows and columns
print(DF.shape)

# Print the data in the emails column only
print(DF["Email"])

# Sort the data based on FirstName in ascending order and print the data"""
print(DF.sort_values("FirstName",ascending=True))