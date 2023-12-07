import os
import csv
# get csv file path
pypoll_csv = os.path.join('.', 'Resources', 'election_data.csv')

# initialize variables to track relevant data
voteCount = 0
candidates = []
candidateVotes = []

with open(pypoll_csv, 'r') as pypoll_file:
    # start reading csv and skip header
    reader = csv.reader(pypoll_file, delimiter=',')
    header = next(reader)

    # loop through data rows
    for row in reader:
        voteCount += 1
        candidate = row[2]

        if candidate not in candidates:
            candidates.append(candidate)
            candidateVotes.append(1)
        else:
            candidateIndex = candidates.index(candidate)
            candidateVotes[candidateIndex] += 1

output = os.path.join('Analysis', 'analysis.txt')
with open(output, 'w', newline='') as output_txt:
    writer = csv.writer(output_txt)
    writer.writerow(["Election Results"])
    writer.writerow(["-----------------------------"])
    writer.writerow([f"Total Votes: {voteCount}"])
    writer.writerow(["-----------------------------"])
    for i in range(len(candidates)):
        votes = candidateVotes[i]
        writer.writerow([f"{candidates[i]}: {round((votes / voteCount) * 100, 2)}% ({votes})"])
    writer.writerow(["-----------------------------"])
    mostVotesIndex = candidateVotes.index(max(candidateVotes))
    winner = candidates[mostVotesIndex]
    writer.writerow([f"Winner: {winner}"])
    writer.writerow(["-----------------------------"])

print("Election Results")
print("-----------------------------")
print(f"Total Votes: {voteCount}")
print("-----------------------------")
for i in range(len(candidates)):
    votes = candidateVotes[i]
    print(f"{candidates[i]}: {round((votes / voteCount) * 100, 2)}% ({votes})")
print("-----------------------------")
mostVotesIndex = candidateVotes.index(max(candidateVotes))
winner = candidates[mostVotesIndex]
print(f"Winner: {winner}")
print("-----------------------------")