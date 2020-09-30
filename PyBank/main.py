# Modules
import os
import csv

# Set path for the file
csvpath = os.path.join('.', 'Resources', 'budget_data.csv')

# Set months as a list
# Set variables to zero

months = []
GPI_month = ""
GPD_month = ""
total_profits_losses = 0
total_profit_change = 0
previous_profit = 0
profit_difference = 0
average_profit_change = 0
greatest_profit_increase = 0
greatest_profit_decrease = 0

# Open CSV
with open(csvpath, 'r') as budget_csv_file:
    csv_reader = csv.reader(budget_csv_file, delimiter= ",")

#Skip header row
    csv_header = next(csv_reader)

#Print title for Analysis
    print("Financial Analysis")
    print("----------------------------")

# Create for loop
    first_row = True
    for row in csv_reader:
        months.append(row[0])
        total_profits_losses += int(row[1])

        if not first_row:
            profit_difference = int(row[1])- previous_profit
            total_profit_change += profit_difference

            if profit_difference > greatest_profit_increase:
                GPI_month = row[0]
                greatest_profit_increase = profit_difference
        
            if profit_difference < greatest_profit_decrease:
                GPD_month = row[0]
                greatest_profit_decrease = profit_difference


        previous_profit = int(row[1])
        first_row = False

num_months = (len(months))
print("Total Months: " + str(num_months))
print("Total: " + str(total_profits_losses))
average_profit_change = total_profit_change / (num_months - 1)
print("Average Change: " + str(average_profit_change))
print("Greatest Increase in Profits: " + str(GPI_month) + "$" + str(greatest_profit_increase))
print("Greatest Decrease in Profits: " + str(GPD_month) + "$" + str(greatest_profit_decrease))

output_path = os.path.join(".", "Analysis", "PyBankReport.txt")


with open(output_path, 'w') as txtfile:

    txtfile.write("Financial Analysis"+"\n")
    txtfile.write("----------------------------"+"\n")
    txtfile.write("Total Months: " + str(num_months)+"\n")
    txtfile.write("Total: " + str(total_profits_losses)+"\n")
    txtfile.write("Average Change: " + str(average_profit_change)+"\n")
    txtfile.write("Greatest Increase in Profits: " + str(GPI_month) + " " + str(greatest_profit_increase)+"\n")
    txtfile.write("Greatest Decrease in Profits: " + str(GPD_month) + " " + str(greatest_profit_decrease)+"\n")

txtfile.close()