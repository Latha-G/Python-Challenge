import os
import csv

Candidate_list = []
vote_count_list = []
Percentagevotes_list = []
output2 = []

total_votes = 0
ind_count = 0

# Path to collect data from the Resources folder
csvfile_to_read = os.path.join('Resources', 'Election_Data_HW.csv')

# Path to upload output
txt_file_to_upload = os.path.join('Analysis' , 'PyPoll-Results.txt')

# Read in the CSV file
with open(csvfile_to_read, 'r') as csvfilehandle:

    # Split the data on commas
    csvfile_to_read = csv.reader(csvfilehandle, delimiter = ',')

    header = next(csvfile_to_read)

    # Loop through the data in csv file
    for row in csvfile_to_read:
        
        # Count Total votes
        total_votes = total_votes + 1
        
        # Create unique list of Candidates and assigning zeros to other lists
        if row[2] not in Candidate_list:
            Candidate_list.append(row[2])
            vote_count_list.append(0)
            Percentagevotes_list.append(0)
            output2.append(0)
        
        # Find votecount of each candidate
        for x in range(0,len(Candidate_list)):
            if row[2] == Candidate_list[x]:
                vote_count_list[x] = vote_count_list[x] + 1
                
        # Find Percentage of votes for each candidate
        for x in range(0,len(Candidate_list)):
            Percentagevotes_list[x] = round(vote_count_list[x]/total_votes * 100,0)
    

    # Find Max Vote Count
    max_count_index = vote_count_list.index(max(vote_count_list))
    Winner = Candidate_list[max_count_index]


with open(txt_file_to_upload, 'w') as txtfile:
    
    # Print Total votes
    output1 = (f'\n\nElection Results: \n\n'
        f'-----------------------------\n'
        f'Total Votes: {total_votes} \n'
        f'-----------------------------\n')
    print(output1)
    txtfile.write(output1)
        
    # Print Candidate name and VoteCount
    for x in range(0,len(Candidate_list)):
        output2[x] = (f'\n{Candidate_list[x]}: {Percentagevotes_list[x]:.3f}%  ({vote_count_list[x]})\n')
        print(output2[x])
        txtfile.write(output2[x])
        
    # Print Winner name
    output3 = (f'\n-----------------------------\n'
        f'Winner: {Winner} \n'
        f'-----------------------------\n')
    print(output3)
    txtfile.write(output3)

'''
Solution:

 Election Results
 -------------------------
 Total Votes: 3521001
 -------------------------
 Khan: 63.000% (2218231)
 Correy: 20.000% (704200)
 Li: 14.000% (492940)
 O'Tooley: 3.000% (105630)
 -------------------------
 Winner: Khan
 -------------------------
 
 '''
