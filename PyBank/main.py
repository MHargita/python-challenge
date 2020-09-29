# Modules
import os
import csv

# Set path for the file
csvpath = os.path.join('.', 'Resources', 'budget_data.csv')

# Set months as a list
# Set variables to zero

months = []
total_profits_losses = 0
total_profit_change = 0
previous_profit = 0
profit_difference = 0

# Open CSV
with open(csvpath, 'r') as budget_csv_file:
    csv_reader = csv.reader(budget_csv_file, delimiter= ",")

#Skip header row
    csv_header = next(csv_reader)

# Create for loop
    for row in csv_reader:
        months.append(row[0])
        total_profits_losses += int(row[1])
        total_profit_change += int(row[1])-previous_profit
        profit_difference = int(row[1])- previous_profit
        previous_profit = int(row[1])

# Print out to check
print(len(months))
print(total_profits_losses)
print(total_profit_change)
print(profit_difference)
print(previous_profit)







# Find the total number of months included in the dataset

# Find the net total amount of "Profit/Losses" over the entire period

# Find the average of the changes in "Profit/Losses" over the entire period

# Find the greatest increase in profits (date and amount) over the entire period

# Find the greatest decrease in losses (date and amount) over the entire period

# The final script should both print the analysis to the terminal and export a text file with the results