# Modules
import os
import csv

# Set path for the file
csvpath = os.path.join('Resources', 'budget_data.csv')

# Define the function and have it accept the 'profit_losses' as its sole parameter
def print_budget_stats(bank_data):
    date = str(bank_data[0])
    profit_losses = int(bank_data[1])
    
def total_profitlosses(bank_data):
    profit_losses = sum(int(bank_data[1]))


    # Total profit_losses can be found by adding the sum together
       

# Open CSV
with open(csvpath) as budget_csv_file:
    csvreader = csv.reader(budget_csv_file, delimiter=",")


print(print_budget_stats(bank_data))
# Find the total number of months included in the dataset
 
        


# Find the net total amount of "Profit/Losses" over the entire period

# Find the average of the changes in "Profit/Losses" over the entire period

# Find the greatest increase in profits (date and amount) over the entire period

# Find the greatest decrease in losses (date and amount) over the entire period

# The final script should both print the analysis to the terminal and export a text file with the results