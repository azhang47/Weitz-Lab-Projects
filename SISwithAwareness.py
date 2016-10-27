import numpy as np

network = [[0,1,0,0,0],
           [1,0,1,1,1],
           [0,1,0,0,0],                 #generalize to multiple nodes, storage not print, another python file with distancing model
           [0,1,0,0,0],                 #random number of nodes and random states
           [0,1,0,0,0]]                 #the network can be made manually
                                        #bc symmetric networks i=j, j=i, then just iterate through half of the matrix i>j
                                        #might need more functions for network generation
priorstate = [0,1,0,0,0]                #look into making plots vs lists
state = [0,1,0,0,0]
beta = 0.3 #infection rate
delta = 0.2 #healing rate

#def SISwithAwareness():
iteration = 50
print state
for time in range(0,iteration):
    for i in range(0,5):
        if priorstate[i] == 0:  #check if node is healthy
            probability = 1     #reset probability
            for k in range(0,5):        
                if network[i][k] == 1:  #iterate through its neighbors
                    if priorstate[k] == 1:  #check if neighbor is infected
                        probability = (1-beta)*probability  #infected neighbor increases chance of sickness
                        flip = np.random.uniform(0.0,1.0)
                        if probability < flip:
                            state[i] = 1    #node is infected
        if priorstate[i] == 1:  #checks if node is already infected
            flip = np.random.uniform(0.0,1.0)
            if delta > flip:    #flips to see if node heals
                state[i] = 0
    print state
    for element in range(0,5):
        priorstate[element] = state[element]
    

#        for j in range(0,5):
#            if network[i][j] == 0:
#                probability = 1
#                try:
#                  if network[i][j-1] == 1: 
#                        probability = (1-beta)*probability
#                except:
#                    pass
#                try:
#                   if network[i][j+1] == 1:
#                        probability = (1-beta)*probability #if multipe neighbors sick, higher chance of sickness
#                except:
#                    pass

#            flip = np.random.uniform(0.0,1.0)
#            if probability < flip:
#                if network[i][j] == 0:
#                    state[i] = 1
#            if network[i][j] == 1:
#                if delta > flip:
#                    state[i] = 0
#    print state
#    priorstate = state






