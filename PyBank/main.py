main.py

#Import CSV
import os
import csv
csvpath = os.path.join('Starter_Code/Resources_PyBank/budget_data.csv')
print(csvpath)

#Load CSV Module for improved reading; read & view headers
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    for row in csvreader:
        print(row)  

#Count total # of months
    count = 0
    for row in csvreader:
        count += 1
        count -= 1
    print("Total Months: " + str(count))
    



#Sum Profits, Sum Losses, Subtract Losses from Profits


#Show changes in Profit/Losses, Avgerage of changes


#Date & amount of greatest increase


#Date and amount greatest decreas

