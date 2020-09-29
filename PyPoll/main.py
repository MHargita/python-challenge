# Modules
import os
import csv

# Set path for the file
csvpath = os.path.join('.', 'Resources', 'election_data.csv')

with open(csvpath, 'r') as election_data_file:
    csv_reader = csv.reader(election_data_file, delimiter= ",")



