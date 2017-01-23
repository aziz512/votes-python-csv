import sys
import csv

csv_path = sys.argv[1]
precinct_to_votes = {} #final data object
precincts = [] #list of unique precints

def displayPrecinct(precinctStr):
    print(precinctStr)
    for key in precinct_to_votes[precinctStr]:
        #TODO: use string format
        print ('   ' + key + ' ' + str(precinct_to_votes[precinctStr][key]) + ' votes')

with open(csv_path) as file:
    rows = list(csv.reader(file))
    #remove header
    del rows[0]
    #getting the list of unique precincts
    for i in range(len(rows)):
        if not rows[i][1] in precincts:
            precincts.append(rows[i][1])            
    
    #getting the list of candidates for each unique precinct
    for precinct in precincts:
        precinct_candidates = list(filter(lambda x: x[1] == precinct and x[2] == 'President',rows))
        candidates = {}
        #avoid duplicate names
        for candidate in precinct_candidates:
            if not candidate[5] in candidates:
                candidates[candidate[5]] = candidate[6]
            else:
                #if duplicate just add up votes
                candidates[candidate[5]] = int(candidates[candidate[5]]) + int(candidate[6])
        
        #saving candidates dict into the main data output 
        precinct_to_votes[precinct] = candidates
    
    #check if user wants to filter by precinct name (which is passed as a third parameter)
    if len(sys.argv) > 2:
        displayPrecinct(sys.argv[2])
    else:
        #if filter not given, display all precincts
        for precinct in precinct_to_votes:
            displayPrecinct(precinct)
        
