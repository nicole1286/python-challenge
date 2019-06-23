import os
import csv
import statistics

PyPoll = os.path.join('Resources', 'election_data.csv')

voter_id = 0
votes = 0
candidate = ["Khan", "Corry", "Li", "O'Tooley"]
print("Election Results")
print("------------------------------")
with open  (PyPoll, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    for row in csvreader:
        voter_id += 1
       # candidate + int(row[2])
    #candidate.count(sum)?

    print(f"Total Votes: {voter_id}")
    print("--------------------------")
    print(*candidate, sep = "\n")
    #winner = (statistics.mode(candidate))
    #print("Winner: {winner}")