import os
import csv

# Path to collect data from the folder
electdata = os.path.join('election_data.csv')


total_votes_cast = 0
list_of_candidates = []
candidate_vote_counter = {}
winner_name = ""
winner_votes = 0 

# Read in the CSV file
with open(electdata, 'r', newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #This skips the first row of the CSV file.
    next(csvreader, None)  

    for line in csvreader:
        #The total number of votes cast included in the dataset    
        total_votes_cast = total_votes_cast + 1
        
        #A complete list of candidates who received votes
        current_candidate = line[2]
        if current_candidate not in list_of_candidates:
            list_of_candidates.append(current_candidate)
            candidate_vote_counter[current_candidate] = 0
        else:
            candidate_vote_counter[current_candidate] = candidate_vote_counter[current_candidate] + 1    
        #print(list_of_candidates)    
        #The total number of votes each candidate won
        #print(candidate_vote_counter)
        
file = open("pypollscript.txt","w")
print("Poll Analysis")
print(str(total_votes_cast) + " votes were cast.")
file.write("Poll Analysis"+'\n'"--------------" '\n' + 
           str(total_votes_cast) + " votes were cast."'\n')
print("Here is the list of candidates, their vote percentage, and total number of votes:")
file.write('\n'"Here is the list of candidates, their vote percentage, and total number of votes:"'\n')
for candidate in candidate_vote_counter:
        
    candidate_votes = candidate_vote_counter.get(candidate)
    #print(candidate_votes)
        
    
    percentageofvotes = round(((candidate_votes / total_votes_cast) *100),3)
    print(candidate + ": " + str(percentageofvotes) + '% ' + '('+ str(candidate_votes) +')')
    file.write('\n'+ candidate + ": " + str(percentageofvotes) + '% ' + '('+ str(candidate_votes) +')''\n')    
    #The winner of the election based on popular vote
    if candidate_votes > winner_votes:
        winner_votes = candidate_votes
        winner_name = candidate
            
print("The winner of our election is: " + winner_name)
file.write('\n'"The winner of our election is: " + winner_name +'\n')
#Export a text file with the results
file.close()