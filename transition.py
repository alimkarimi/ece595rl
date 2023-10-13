import numpy as np
grid = np.zeros((4,4))


grid_actions = np.array([['r', 'r', 'd', 'u'], 
                         ['u', 'u', 'r', 'u'],
                        ['u', 'l', 'r', 'u'], 
                         ['u', 'u', 'r', 'u']])

grid_actions_test = np.array([['l', 'l', 'l', 'l'], 
                         ['l', 'l', 'l', 'l'],
                        ['l', 'l', 'l', 'l'], 
                         ['l', 'l', 'l', 'l']])


def computeTransitionFunction(grid_actions):
    P = np.zeros((16,16))
    for row in range(grid_actions.shape[0]):
        for col in range(grid_actions.shape[1]):
            policy = grid_actions[row,col] #up, down, left, right will be the policy. mapping from state to action
            #check if policy has a boundary or unreachable state:
            current_state = row * 4 + col
            prob_stay = 0.0
            ### POLICY TO THE RIGHT ###
            if policy == 'r':
                temp_col = col + 1
                if (temp_col <= 3) and (temp_col >= 0): #valid
                    next_state = (row, col + 1)
                    next_state = row * 4 + col + 1
                    P[current_state, next_state] = 0.85
                if (temp_col > 3) or (temp_col < 0): # invalid move
                    P[current_state, current_state] = 0.85
                # check if other moves are valid:
                # start with up:
                if (row - 1 >= 0) and (row - 1 <=3):
                    # this transition has a 0.05 probability
                    next_state = (row - 1) * 4 + col
                    if (next_state != 10):
                        P[current_state, next_state] = 0.05
                    else: 
                        P[current_state, current_state] += 0.05
                else:
                    P[current_state, current_state] += 0.05

                # check down:
                if (row + 1 >= 0) and (row + 1 <=3):
                    # this transition has a 0.05 probability
                    next_state = (row + 1) * 4 + col
                    if (next_state != 10):
                        P[current_state, next_state] = 0.05
                    else: 
                        P[current_state, current_state] += 0.05
                else:
                    P[current_state, current_state] += 0.05

                # check left
                if (col - 1 >= 0) and (col - 1 <=3):
                    # this transition has a 0.05 probability
                    next_state = row * 4 + col - 1
                    if (next_state != 10):
                        P[current_state, next_state] = 0.05
                    else: 
                        P[current_state, current_state] += 0.05
                else:
                    P[current_state, current_state] += 0.05



            ### POLICY TO THE LEFT ###
            if policy == 'l':
                temp_col = col - 1
                if (temp_col <= 3) and (temp_col >= 0): #valid
                    next_state = (row, col -1)
                    next_state = row * 4 + col - 1
                    P[current_state, next_state] = 0.85
                if (temp_col > 3) or (temp_col < 0): # invalid move
                    P[current_state, current_state] = 0.85
                #check if other moves are valid:
                # start with up:
                if (row - 1 >= 0) and (row - 1 <=3):
                    # this transition has a 0.05 probability
                    next_state = (row - 1) * 4 + col
                    if (next_state != 10):
                        P[current_state, next_state] = 0.05
                    else: 
                        P[current_state, current_state] += 0.05
                else:
                    P[current_state, current_state] += 0.05

                # check down:
                if (row + 1 >= 0) and (row + 1 <=3):
                    # this transition has a 0.05 probability
                    next_state = (row + 1) * 4 + col
                    if (next_state != 10):
                        P[current_state, next_state] = 0.05
                    else: 
                        P[current_state, current_state] += 0.05
                else:
                    P[current_state, current_state] += 0.05

                # check right:
                if (col +1 >= 0) and (col +1 <=3):
                    # this transition has a 0.05 probability
                    next_state = row * 4 + col + 1
                    if (next_state != 10):
                        P[current_state, next_state] = 0.05
                    else: 
                        P[current_state, current_state] += 0.05
                else:
                    P[current_state, current_state] += 0.05




            if policy == 'u':
                temp_row = row -1
                if (temp_row <= 3) and (temp_row >= 0): #valid
                    next_state = (row - 1) * 4 + col
                    P[current_state, next_state] = 0.85
                if (temp_row > 3) or (temp_row < 0): # invalid move
                    prob_stay = prob_stay + 0.05 #hold this value. We need to know the total invalid moves
                    P[current_state, current_state] = 0.85
                # check if other moves are valid:
                # check down:

                if (row + 1 >= 0) and (row + 1 <=3):
                    # this transition has a 0.05 probability
                    next_state = (row + 1) * 4 + col
                    if (next_state != 10):
                        P[current_state, next_state] = 0.05
                    else: 
                        P[current_state, current_state] += 0.05
                else:
                    P[current_state, current_state] += 0.05
                # check right:

                if (col +1 >= 0) and (col +1 <=3):
                    # this transition has a 0.05 probability
                    next_state = row * 4 + col + 1
                    if (next_state != 10):
                        P[current_state, next_state] = 0.05
                    else: 
                        P[current_state, current_state] += 0.05
                else:
                    P[current_state, current_state] += 0.05
                # check left

                if (col - 1 >= 0) and (col - 1 <=3):
                    # this transition has a 0.05 probability
                    next_state = row * 4 + col - 1
                    if (next_state != 10):
                        P[current_state, next_state] = 0.05
                    else: 
                        P[current_state, current_state] += 0.05
                else:
                    P[current_state, current_state] += 0.05

            if policy == 'd':
                temp_row = row + 1
                if (temp_row <= 3) and (temp_row >= 0): #valid
                    next_state = (row + 1) * 4 + col
                    P[current_state, next_state] = 0.85
                if (temp_row > 3) or (temp_row < 0): # invalid move
                    P[current_state, current_state] = 0.85
                # check if other moves are valid:\
                # check right:

                if (col +1 >= 0) and (col +1 <=3):
                    # this transition has a 0.05 probability
                    next_state = row * 4 + col + 1
                    if (next_state != 10):
                        P[current_state, next_state] = 0.05
                    else:
                        P[current_state,current_state] += 0.05
                else:
                    P[current_state, current_state] += 0.05
                # check left

                if (col - 1 >= 0) and (col - 1 <=3):
                    # this transition has a 0.05 probability
                    next_state = row * 4 + col - 1
                    if (next_state != 10):
                        P[current_state, next_state] = 0.05
                    else:
                        P[current_state,current_state] += 0.05
                else:
                    P[current_state, current_state] += 0.05

                # check up:
                if (row - 1 >= 0) and (row - 1 <=3):
                    # this transition has a 0.05 probability
                    next_state = (row - 1) * 4 + col
                    if (next_state != 10):
                        P[current_state, next_state] = 0.05
                    else:
                        P[current_state,current_state] += 0.05
                else:
                    P[current_state, current_state] += 0.05

    # all actions in the cell with the lightning bolt and treasure chest will keep the agent in the current cell. 
    # this means P[3,3] = 1, P[5,5] = 1
    P[3] = np.array([0, 0, 0 , 1, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0])
    P[5] = np.array([0, 0, 0 , 0, 0, 1, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0])
    
    return P

P = computeTransitionFunction(grid_actions) # compute the transition function given grid_actions above.
