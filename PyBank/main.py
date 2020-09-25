# Modules
import os
import csv

# Set path for the file
csv_file = os.path.join("..", "resources", "budget_data.csv")

# Open CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

# Find the total number of months included in the dataset
    for row in csvreader:
        


# Find the net total amount of "Profit/Losses" over the entire period

# Find the average of the changes in "Profit/Losses" over the entire period

# Find the greatest increase in profits (date and amount) over the entire period

# Find the greatest decrease in losses (date and amount) over the entire period

# The final script should both print the analysis to the terminal and export a text file with the results