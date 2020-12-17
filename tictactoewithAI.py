import tkinter as tk
from tkinter import messagebox
from random import randrange

window = tk.Tk()
buttons = [[tk.Button() for i in range(3)] for j in range(3)]
player = 'X'
ai = 'O'

human_moves_first = True

# fill 2d list with blank buttons with that call onClick and pass their indices in the list when pressed
for i in range(3):
    for j in range(3):
        buttons[i][j] = (tk.Button(window, text=' ', 
                         command = lambda i = i, j = j: onClick(i, j), width = 10, height = 10))
        buttons[i][j].grid(row = i, column = j)

             
        
def onClick(i,j):
    # human move
    if(buttons[i][j]['text'] == ' '):
        buttons[i][j]['text'] = player
    is_game_over()
    # ai move
    AI()
    is_game_over()



#returns True if win detected, False otherwise        
def is_game_over():
    win = False;
    winner = ' '
    spaces_filled_ctr = 0
    
    for i in range(3):
        # check for row win
        if(buttons[i][0]['text'] == buttons[i][1]['text'] == buttons[i][2]['text'] != ' '):
            winner = buttons[i][0]['text']
            win = True
        # check for column win
        if(buttons[0][i]['text'] == buttons[1][i]['text'] == buttons[2][i]['text'] != ' '):
            winner = buttons[0][i]['text']
            win = True
        # count filled spaces for stalemate detection
        for j in range(3):
            if(buttons[i][j]['text'] != ' '):
                spaces_filled_ctr += 1
    
    # check each diagonal for win
    if(buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != ' '):
        winner = buttons[0][0]['text']
        win = True
    if(buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != ' '):
        winner = buttons[0][2]['text']
        win = True 
    
    if(win):
        tk.messagebox.showinfo(title = 'Game Over!', message = winner + ' wins')
        window.destroy()    
    if(spaces_filled_ctr == 9):
        tk.messagebox.showinfo(title = 'Game Over!', message = 'Stalemate')
        window.destroy()    
    
def AI():
    possible_moves = []
    move_values = []
    for i in range(3):
        for j in range(3):
            #traverse array and find all moves available to be made
            if(buttons[i][j]['text'] == ' '):
                # add them to possible moves list
                possible_moves.append([i,j])
                # score them
                move_values.append(evaluate_move(i,j))
    
    #find the highest move value and record its place in the list
    highest_val = 0
    highest_val_idx = 0
    for i in range(len(possible_moves)):
        if(move_values[i] > highest_val):
            highest_val = move_values[i]
            highest_val_idx = i
            
    #this means we're making the first move, so make it random just for fun
    if(highest_val == 0):
        buttons[randrange(3)][randrange(3)]['text'] = ai
    else:
        # make the move with the highest value
        buttons[possible_moves[highest_val_idx][0]][possible_moves[highest_val_idx][1]]['text'] = ai

            
def evaluate_move(i,j):
    value = 0
    opponent_this_row = False;
    opponent_this_col = False;
    opponent_this_diag = False;
    self_this_row = False;
    self_this_col = False;
    self_this_diag = False;
    
    # tune our values for whether we move first or human does
    if(human_moves_first):
        opp_this_rowcoldiag_value = 4
        self_this_rowcoldiag_and_not_opp = 2
        opp_has_one_in_row_but_not_col = 1
    else:
        opp_this_rowcoldiag_value = 1
        self_this_rowcoldiag_and_not_opp = 3
        opp_has_one_in_row_but_not_col = 2
    
    # loop through board examining comaparing what each space contains to this potential move
    for x in range(3):
        for y in range(3):
            # we want to block the opponent if they have one in this row/col/diagonal
            if(buttons[x][y]['text'] == player):
                if(x == i):
                    opponent_this_row = True
                    value += opp_this_rowcoldiag_value
                if(y == j):
                    opponent_this_col = True
                    value += opp_this_rowcoldiag_value
                if(in_same_diagonal([[x,y],[i,j]])):
                    opponent_this_diag = True
                    value += opp_this_rowcoldiag_value
            # we want to complete our row if we already have one in this 
            # row/col/diagonal and the opponent doesn't        
            if(buttons[x][y]['text'] == ai):
                if(x == i):
                    self_this_row = True
                    if(not(opponent_this_row)):
                        value += self_this_rowcoldiag_and_not_opp
                if(y == j):
                    self_this_col = True
                    if(not(opponent_this_col)):
                        value += self_this_rowcoldiag_and_not_opp   
                if(in_same_diagonal([[x,y],[i,j]])):
                    self_this_diag = True
                    if(not(opponent_this_diag)):
                        value += self_this_rowcoldiag_and_not_opp 
              
    # placing a mark when the opponent has one in the row but not the column/diagonal, 
    # or vice versa, both blocks and gives us a chance to take the row/col/diagonal
    if(opponent_this_row != opponent_this_col  or 
       opponent_this_row != opponent_this_diag or
       opponent_this_col != opponent_this_diag):
        value += opp_has_one_in_row_but_not_col
 
    return value
    
# pass this function a 2d list containing two lists of two ints, each list being 
# a coordinate pair in the grid
def in_same_diagonal(two_coords_list):
    pair_1 = two_coords_list[0]
    pair_2  = two_coords_list[1]
    diag_1 = [[0,0],[1,1],[2,2]]
    diag_2 = [[0,2],[1,1],[2,0]]
    
    # if they aren't in the same diagonal, also return false    
    if((pair_1 in diag_1) and (pair_2 in diag_1)):
        return True
    
    if((pair_1 in diag_2) and (pair_2 in diag_2)):
        return True    
    
    return False
        
if(not(human_moves_first)):
    AI()     
   
window.mainloop()


    
