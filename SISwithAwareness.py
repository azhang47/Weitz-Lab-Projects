import numpy as np

network = [[0,1,0,0,0],
           [1,0,1,1,1],
           [0,1,0,0,0],
           [0,1,0,0,0],
           [0,1,0,0,0]]

state = [0,0,0,0,0]
priorstate = [0,0,0,0,0]

beta = 0.5 #infection rate
delta = 0.5 #healing rate

#def SISwithAwareness():
iteration = 10
print state
for time in range(0,iteration):
    for i in range(0,5):
        for j in range(0,5):
            if network[i][j] == 0:
                probability = 1
                try:
                    if network[i][j-1] == 1: 
                        probability = (1-beta)*probability
                except:
                    pass
                try:
                    if network[i][j+1] == 1:
                        probability = (1-beta)*probability #if multipe neighbors sick, higher chance of sickness
                except:
                    pass
            flip = np.random.uniform(0.0,1.0)
            if probability < flip:
                if network[i][j] == 0:
                    state[i] = 1
            if network[i][j] == 1:
                if delta > flip:
                    state[i] = 0
    print state
    priorstate = state



#a=b=c=d=e=1
#array1 = [[b],[a,c,d,e],[b],[b],[b]]
#for a in (0,5):
#    for b in (0,5):
#        if array[a][b] == 1:
#            array1[a][0] = array[a][b]


#def SISwithAwareness():
#    s_i = 0
#    t = 1
#    delta = np.random.uniform(0.0,1.0)  
#    beta = np.random.uniform(0.0,0.5)   
#    for time in range(0,t):
#        for i in range(0,5):
#            if  
#                p_i = 1   #probability of staying healthy initially
#                for a in range(0,5):
#                    for b in range(0,5):
#                        for array1[x][y] == 1: #np.apply_along_axis()
#                            p = (1-beta)*p
#                        p_i = (0,1) #probability of staying healthy in time t+1
#        infected = np.random.random_integers(0,1)   #random number generator
#        if pi-1 < infected & s_i == 0:
#             s_t+1 = 1
#        for i in range (1,n) & list[time]=1:
#            if delta > infected:
#        s(t+1) = 0
#        for i in (0,5);
#            for j in (0,5):
#                if array[i][j] == 1:
#
#        print "a is" + a
#        print "b is" + b
#        print "c is" + c
#        print "d is" + d
#        print "e is" + e


