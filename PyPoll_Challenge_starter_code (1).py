import csv
import os
file_to_load = os.path.join(r"C:\Users\georg\Downloads\election_results.csv")
candidate_options = [] #country names
candidate_votes = {}

with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:


        # 3: Extract the county name from each row.
        candidate_name = row[2]
        #candidate_options = row[1]

        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        

l = list() # votes
m = list()  # %votes

with open(r'C:\Users\georg\Downloads\file_to_save.txt', "w") as txt_file:


  # Print the final vote count (to terminal)
  election_results = (
      f"\nElection Results\n"
      f"-------------------------\n"
      f"Total Votes: {total_votes:,}\n"
      f"-------------------------\n\n"
      f"County Votes:\n")
  print(election_results, end="")

  txt_file.write(election_results)
  for candidate_name in candidate_votes:

    votes = candidate_votes.get(candidate_name)
    vote_percentage = float(votes) / float(total_votes) *100

    candidate_results = (
        f"{candidate_name} : {votes} --- {vote_percentage :1f}%"
    )
    print(candidate_results)
    txt_file.write(candidate_results)

    l.append(votes)
    m.append(vote_percentage)

  if l[0] > l[1] :
    if l[0] > l[2]:
      winning_count = l[0]
    else:
      winning_count = l[2]
  else :
    winning_count = l[1]

  if m[0] > m[1] :
    if m[0] > m[2]:
      winning_percentage = m[0]
    else:
      winning_percentage = m[2]
  else :
    winning_percentage = m[1]

  for name,votes in candidate_votes.items():
    if votes == winning_count:
      winning_candidate = name
  winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
  print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
  txt_file.write(winning_candidate_summary)


