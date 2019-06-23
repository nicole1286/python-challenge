import os
import csv

#path to collect data from folder
budget_PyBank = os.path.join('.', 'Resources', 'budget_data.csv')
print("Financial Analysis")
print("-------------------------")
months = 0
total = 0
average = 0
with open (budget_PyBank, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    for row in csvreader:
        months += 1
        total += int(row[1])
        max = 1170595
        min = -1196225
    
    print(f"Total Months: {months}")
    print(f"Total: ${total}")
    average = round(int(total)/int(months), 2)

    print(f"Average income: ${average}")
#Format Integer in python- everything for specific #'s not cvs results
        # if total == max:
        # print("Greatest Profit: "(row))
        # if row[1] == min:
        # print("Greatest Loss: " (row))

    
