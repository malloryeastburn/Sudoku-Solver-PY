from tkinter import *
import tkinter.font as tkFont
from functools import partial
root = Tk()
root.title("Sudoku Solver")
root.iconbitmap("C:\\Users\\mallo\\OneDrive\\Desktop\\images\\sudokuIcon.ico")
fontStyle = tkFont.Font(family="Lucida Grande", size=30)
#Default board
board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]
button_identities = []

def select_number(num):
    global number
    number = num +1
    return
def assign_number(i,j):
    if i == 0:
        objectName = (button_identities[j])
    else:
        objectName = (button_identities[j+len(board[0]) * i])
    objectName.configure(text=number)
    return
for i in range(len(board)):
    for j in range(len(board[0])):
        cur_button = "cur_button" + str(i) + str(j)
        if i // 3 != 1 and j // 3 != 1 or i // 3 == 1 and j // 3 == 1:
            rlf="solid"
        else:
            rlf="raised"
        cur_button = Button(root, font=fontStyle, width=3, height=1, relief=rlf, command=partial(assign_number,i,j))
        button_identities.append(cur_button)
        cur_button.grid(row=i, column=j)
for i in range(len(board[0])):
    cur_num="num" + str(i)
    cur_num = Button(root, text=i+1, font=fontStyle, width=3, height=1, borderwidth=3, relief="solid", command=partial(select_number,i))
    cur_num.grid(row=len(board)+1, column=i)
blank = Label(root, text="")   
blank.grid(row=9, column=0)
def clear_board():
    for item in button_identities:
        item.configure(text='')
    return
def solve_board():

    return
btn_empty = Button(root, text="Clear Board", font=fontStyle, width=12, height=1, relief="solid", command=clear_board)
btn_solve = Button(root, text="Solve", font=fontStyle, width=12, height=1, relief="solid", command=solve_board)
btn_empty.grid(row=len(board)+2, column=0, columnspan=4)
btn_solve.grid(row=len(board)+2, column=5, columnspan=4)
root.mainloop()

#Backtracking function that solves the board. Calls itself when a solution is invalid until the board is solved
def solve(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find
    for i in range(1, 10):
        if valid(board, i, (row, col)):
            board[row][col] = i
            if solve(board):
                return True
            board[row][col] = 0
    return False

#checks to see if a number is valid
def valid(board, num, pos):
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False
    box_x = pos[1] // 3 # column
    box_y = pos[0] // 3 # row 
    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if board[i][j] == num and (i,j) != pos:
                return False
    return True

#Displays the board in a readable way
def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - -")
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print("| ", end="")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")
                
#Finds the next empty space
def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
    return None

#Prints the board before it is solved
print("Unsolved:")       
print_board(board)

#If solved, prints board, else: Display no solution
if solve(board) == True:
    print("\nSolved:")
    print_board(board)
else:
    print("\nNo solution")