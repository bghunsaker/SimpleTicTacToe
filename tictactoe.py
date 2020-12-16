import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
buttons = [[tk.Button() for i in range(3)] for j in range(3)]
playerTurn = 'X'


# fill 2d list with blank buttons with that call onClick and pass their indices in the list when pressed
for i in range(3):
    for j in range(3):
        buttons[i][j] = (tk.Button(window, text=' ', 
                         command = lambda i = i, j = j: onClick(i, j), width = 10, height = 10))
        buttons[i][j].grid(row = i, column = j)

def onClick(i,j):
    global playerTurn
    if(buttons[i][j]['text'] == ' '):
        buttons[i][j]['text'] = playerTurn
    if(won()):
        tk.messagebox.showinfo(title = 'Game Over!', message = playerTurn + ' wins')
        window.destroy()
    if(playerTurn == 'X'):
        playerTurn = 'O'
    else:
        playerTurn = 'X'

#returns True if win detected, False otherwise        
def won():
    for i in range(3):
        if((buttons[i][0]['text'] == buttons[i][1]['text'] == buttons[i][2]['text'] != ' ') or
           (buttons[0][i]['text'] == buttons[1][i]['text'] == buttons[2][i]['text'] != ' ')):
            return True
    if((buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != ' ') or
       (buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != ' ')):
        return True
    return False;
        
window.mainloop()


    
