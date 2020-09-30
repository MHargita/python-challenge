# Modules
import os
import csv

# Set path for the file
csvpath = os.path.join('.', 'Resources', 'election_data.csv')

with open(csvpath, 'r') as election_data_file:
    csv_reader = csv.reader(election_data_file, delimiter= ",")

#Skip header row
    csv_header = next(csv_reader)

#Set variables, candidate_votes as empty dictionary
    Total_votes = 0
    result = ""
    Candidate_votes = {}

    print("Election Results")

#For loop to determine total amount of votes
    for row in csv_reader:
  
        Total_votes += 1
        if row[2] in Candidate_votes:
            Candidate_votes[row[2]] += 1

        else:
            Candidate_votes[row[2]] = 1

    print("-------------------------")
    print("Total Votes: " + str(Total_votes))
    print("-------------------------")

# For loop with dictionary
    for candidate, vote_count in Candidate_votes.items():
        vote_percentage = vote_count * 100 / Total_votes
        result = result + (candidate + ": " + str(round(vote_percentage, 3)) + "% (" + str(vote_count) + ")\n")

# To determine winner get max votes    
    winner = max(Candidate_votes, key = Candidate_votes.get)

    print(result.rstrip("\n"))
    print("-------------------------")
    print("Winner: " + winner)
    print("-------------------------")

# Export to text file
# Set Path 
    output_path = os.path.join(".", "Analysis", "PyPollReport.txt")

    with open(output_path, 'w') as txtfile:

        txtfile.write("Election Results"+"\n")
        txtfile.write("-------------------------"+"\n")
        txtfile.write("Total Votes: " + str(Total_votes) +"\n")
        txtfile.write("-------------------------"+"\n")
        txtfile.write(result)
        txtfile.write("-------------------------"+"\n")
        txtfile.write("Winner: " + winner +"\n")
        txtfile.write("-------------------------"+"\n")

    txtfile.close()