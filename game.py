from tkinter import *
import tkinter.font as tkFont
root = Tk()
root.title("Sudoku Solver")
root.iconbitmap("C:\\Users\\mallo\\OneDrive\\Desktop\\images\\sudokuIcon.ico")
fontStyle = tkFont.Font(family="Lucida Grande", size=30)

def build_board_display():
    
    def select_number(num):
        global number
        number = num
    def assign_number(object):
        object['text'] = number

    box_00 = Button(root, font=fontStyle, width=2, height=1, relief="solid", command=lambda: assign_number(box_00))
    box_01 = Button(root, font=fontStyle, width=2, height=1, relief="solid", command=lambda: assign_number(box_01))
    box_02 = Button(root, font=fontStyle, width=2, height=1, relief="solid", command=lambda: assign_number(box_02))
    box_03 = Button(root, font=fontStyle, width=2, height=1, relief="sunken", command=lambda: assign_number(box_03))
    box_04 = Button(root, font=fontStyle, width=2, height=1, relief="sunken", command=lambda: assign_number(box_04))
    box_05 = Button(root, font=fontStyle, width=2, height=1, relief="sunken", command=lambda: assign_number(box_05))
    box_06 = Button(root, font=fontStyle, width=2, height=1, relief="solid", command=lambda: assign_number(box_06))
    box_07 = Button(root, font=fontStyle, width=2, height=1, relief="solid", command=lambda: assign_number(box_07))
    box_08 = Button(root, font=fontStyle, width=2, height=1, relief="solid", command=lambda: assign_number(box_08))
    box_10 = Button(root, font=fontStyle, width=2, height=1, relief="solid", command=lambda: assign_number(box_10))
    box_11 = Button(root, font=fontStyle, width=2, height=1, relief="solid", command=lambda: assign_number(box_11))
    box_12 = Button(root, font=fontStyle, width=2, height=1, relief="solid", command=lambda: assign_number(box_12))
    box_13 = Button(root, font=fontStyle, width=2, height=1, relief="sunken", command=lambda: assign_number(box_13))
    box_14 = Button(root, font=fontStyle, width=2, height=1, relief="sunken", command=lambda: assign_number(box_14))
    box_15 = Button(root, font=fontStyle, width=2, height=1, relief="sunken", command=lambda: assign_number(box_15))
    box_16 = Button(root, font=fontStyle, width=2, height=1, relief="solid", command=lambda: assign_number(box_16))
    box_17 = Button(root, font=fontStyle, width=2, height=1, relief="solid", command=lambda: assign_number(box_17))
    box_18 = Button(root, font=fontStyle, width=2, height=1, relief="solid", command=lambda: assign_number(box_18))
    box_20 = Button(root, font=fontStyle, width=2, height=1, relief="solid", command=lambda: assign_number(box_20))
    box_21 = Button(root, font=fontStyle, width=2, height=1, relief="solid", command=lambda: assign_number(box_21))
    box_22 = Button(root, font=fontStyle, width=2, height=1, relief="solid", command=lambda: assign_number(box_22))
    box_23 = Button(root, font=fontStyle, width=2, height=1, relief="sunken", command=lambda: assign_number(box_23))
    box_24 = Button(root, font=fontStyle, width=2, height=1, relief="sunken", command=lambda: assign_number(box_24))
    box_25 = Button(root, font=fontStyle, width=2, height=1, relief="sunken", command=lambda: assign_number(box_25))
    box_26 = Button(root, font=fontStyle, width=2, height=1, relief="solid", command=lambda: assign_number(box_26))
    box_27 = Button(root, font=fontStyle, width=2, height=1, relief="solid", command=lambda: assign_number(box_27))
    box_28 = Button(root, font=fontStyle, width=2, height=1, relief="solid", command=lambda: assign_number(box_28))
    box_30 = Button(root, font=fontStyle, width=2, height=1, relief="sunken", command=lambda: assign_number(box_30))
    box_31 = Button(root, font=fontStyle, width=2, height=1, relief="sunken", command=lambda: assign_number(box_31))
    box_32 = Button(root, font=fontStyle, width=2, height=1, relief="sunken", command=lambda: assign_number(box_32))
    box_33 = Button(root, font=fontStyle, width=2, height=1, relief="solid", command=lambda: assign_number(box_33))
    box_34 = Button(root, font=fontStyle, width=2, height=1, relief="solid", command=lambda: assign_number(box_34))
    box_35 = Button(root, font=fontStyle, width=2, height=1, relief="solid", command=lambda: assign_number(box_35))
    box_36 = Button(root, font=fontStyle, width=2, height=1, relief="sunken", command=lambda: assign_number(box_36))
    box_37 = Button(root, font=fontStyle, width=2, height=1, relief="sunken", command=lambda: assign_number(box_37))
    box_38 = Button(root, font=fontStyle, width=2, height=1, relief="sunken", command=lambda: assign_number(box_38))
    box_40 = Button(root, font=fontStyle, width=2, height=1, relief="sunken", command=lambda: assign_number(box_40))
    box_41 = Button(root, font=fontStyle, width=2, height=1, relief="sunken", command=lambda: assign_number(box_41))
    box_42 = Button(root, font=fontStyle, width=2, height=1, relief="sunken", command=lambda: assign_number(box_42))
    box_43 = Button(root, font=fontStyle, width=2, height=1, relief="solid", command=lambda: assign_number(box_43))
    box_44 = Button(root, font=fontStyle, width=2, height=1, relief="solid", command=lambda: assign_number(box_44))
    box_45 = Button(root, font=fontStyle, width=2, height=1, relief="solid", command=lambda: assign_number(box_45))
    box_46 = Button(root, font=fontStyle, width=2, height=1, relief="sunken", command=lambda: assign_number(box_46))
    box_47 = Button(root, font=fontStyle, width=2, height=1, relief="sunken", command=lambda: assign_number(box_47))
    box_48 = Button(root, font=fontStyle, width=2, height=1, relief="sunken", command=lambda: assign_number(box_48))
    box_50 = Button(root, font=fontStyle, width=2, height=1, relief="sunken", command=lambda: assign_number(box_50))
    box_51 = Button(root, font=fontStyle, width=2, height=1, relief="sunken", command=lambda: assign_number(box_51))
    box_52 = Button(root, font=fontStyle, width=2, height=1, relief="sunken", command=lambda: assign_number(box_52))
    box_53 = Button(root, font=fontStyle, width=2, height=1, relief="solid", command=lambda: assign_number(box_53))
    box_54 = Button(root, font=fontStyle, width=2, height=1, relief="solid", command=lambda: assign_number(box_54))
    box_55 = Button(root, font=fontStyle, width=2, height=1, relief="solid", command=lambda: assign_number(box_55))
    box_56 = Button(root, font=fontStyle, width=2, height=1, relief="sunken", command=lambda: assign_number(box_56))
    box_57 = Button(root, font=fontStyle, width=2, height=1, relief="sunken", command=lambda: assign_number(box_57))
    box_58 = Button(root, font=fontStyle, width=2, height=1, relief="sunken", command=lambda: assign_number(box_58))
    box_60 = Button(root, font=fontStyle, width=2, height=1, relief="solid", command=lambda: assign_number(box_60))
    box_61 = Button(root, font=fontStyle, width=2, height=1, relief="solid", command=lambda: assign_number(box_61))
    box_62 = Button(root, font=fontStyle, width=2, height=1, relief="solid", command=lambda: assign_number(box_62))
    box_63 = Button(root, font=fontStyle, width=2, height=1, relief="sunken", command=lambda: assign_number(box_63))
    box_64 = Button(root, font=fontStyle, width=2, height=1, relief="sunken", command=lambda: assign_number(box_64))
    box_65 = Button(root, font=fontStyle, width=2, height=1, relief="sunken", command=lambda: assign_number(box_65))
    box_66 = Button(root, font=fontStyle, width=2, height=1, relief="solid", command=lambda: assign_number(box_66))
    box_67 = Button(root, font=fontStyle, width=2, height=1, relief="solid", command=lambda: assign_number(box_67))
    box_68 = Button(root, font=fontStyle, width=2, height=1, relief="solid", command=lambda: assign_number(box_68))
    box_70 = Button(root, font=fontStyle, width=2, height=1, relief="solid", command=lambda: assign_number(box_70))
    box_71 = Button(root, font=fontStyle, width=2, height=1, relief="solid", command=lambda: assign_number(box_71))
    box_72 = Button(root, font=fontStyle, width=2, height=1, relief="solid", command=lambda: assign_number(box_72))
    box_73 = Button(root, font=fontStyle, width=2, height=1, relief="sunken", command=lambda: assign_number(box_73))
    box_74 = Button(root, font=fontStyle, width=2, height=1, relief="sunken", command=lambda: assign_number(box_74))
    box_75 = Button(root, font=fontStyle, width=2, height=1, relief="sunken", command=lambda: assign_number(box_75))
    box_76 = Button(root, font=fontStyle, width=2, height=1, relief="solid", command=lambda: assign_number(box_76))
    box_77 = Button(root, font=fontStyle, width=2, height=1, relief="solid", command=lambda: assign_number(box_77))
    box_78 = Button(root, font=fontStyle, width=2, height=1, relief="solid", command=lambda: assign_number(box_78))
    box_80 = Button(root, font=fontStyle, width=2, height=1, relief="solid", command=lambda: assign_number(box_80))
    box_81 = Button(root, font=fontStyle, width=2, height=1, relief="solid", command=lambda: assign_number(box_81))
    box_82 = Button(root, font=fontStyle, width=2, height=1, relief="solid", command=lambda: assign_number(box_82))
    box_83 = Button(root, font=fontStyle, width=2, height=1, relief="sunken", command=lambda: assign_number(box_83))
    box_84 = Button(root, font=fontStyle, width=2, height=1, relief="sunken", command=lambda: assign_number(box_84))
    box_85 = Button(root, font=fontStyle, width=2, height=1, relief="sunken", command=lambda: assign_number(box_85))
    box_86 = Button(root, font=fontStyle, width=2, height=1, relief="solid", command=lambda: assign_number(box_86))
    box_87 = Button(root, font=fontStyle, width=2, height=1, relief="solid", command=lambda: assign_number(box_87))
    box_88 = Button(root, font=fontStyle, width=2, height=1, relief="solid", command=lambda: assign_number(box_88))
    num_0 = Button(root, text="1", font=fontStyle, padx=0, pady=0, borderwidth=5, relief="solid", command=lambda: select_number(1))
    num_1 = Button(root, text="2", font=fontStyle, padx=0, pady=0, borderwidth=5, relief="solid", command=lambda: select_number(2))
    num_2 = Button(root, text="3", font=fontStyle, padx=0, pady=0, borderwidth=5, relief="solid", command=lambda: select_number(3))
    num_3 = Button(root, text="4", font=fontStyle, padx=0, pady=0, borderwidth=5, relief="solid", command=lambda: select_number(4))
    num_4 = Button(root, text="5", font=fontStyle, padx=0, pady=0, borderwidth=5, relief="solid", command=lambda: select_number(5))
    num_5 = Button(root, text="6", font=fontStyle, padx=0, pady=0, borderwidth=5, relief="solid", command=lambda: select_number(6))
    num_6 = Button(root, text="7", font=fontStyle, padx=0, pady=0, borderwidth=5, relief="solid", command=lambda: select_number(7))
    num_7 = Button(root, text="8", font=fontStyle, padx=0, pady=0, borderwidth=5, relief="solid", command=lambda: select_number(8))
    num_8 = Button(root, text="9", font=fontStyle, padx=0, pady=0, borderwidth=5, relief="solid", command=lambda: select_number(9))
    blank = Label(root, text="")
    box_00.grid(row=0, column=0)
    box_01.grid(row=0, column=1)
    box_02.grid(row=0, column=2)
    box_03.grid(row=0, column=3)
    box_04.grid(row=0, column=4)
    box_05.grid(row=0, column=5)
    box_06.grid(row=0, column=6)
    box_07.grid(row=0, column=7)
    box_08.grid(row=0, column=8)
    box_10.grid(row=1, column=0)
    box_11.grid(row=1, column=1)
    box_12.grid(row=1, column=2)
    box_13.grid(row=1, column=3)
    box_14.grid(row=1, column=4)
    box_15.grid(row=1, column=5)
    box_16.grid(row=1, column=6)
    box_17.grid(row=1, column=7)
    box_18.grid(row=1, column=8)
    box_20.grid(row=2, column=0)
    box_21.grid(row=2, column=1)
    box_22.grid(row=2, column=2)
    box_23.grid(row=2, column=3)
    box_24.grid(row=2, column=4)
    box_25.grid(row=2, column=5)
    box_26.grid(row=2, column=6)
    box_27.grid(row=2, column=7)
    box_28.grid(row=2, column=8)
    box_30.grid(row=3, column=0)
    box_31.grid(row=3, column=1)
    box_32.grid(row=3, column=2)
    box_33.grid(row=3, column=3)
    box_34.grid(row=3, column=4)
    box_35.grid(row=3, column=5)
    box_36.grid(row=3, column=6)
    box_37.grid(row=3, column=7)
    box_38.grid(row=3, column=8)
    box_40.grid(row=4, column=0)
    box_41.grid(row=4, column=1)
    box_42.grid(row=4, column=2)
    box_43.grid(row=4, column=3)
    box_44.grid(row=4, column=4)
    box_45.grid(row=4, column=5)
    box_46.grid(row=4, column=6)
    box_47.grid(row=4, column=7)
    box_48.grid(row=4, column=8)
    box_50.grid(row=5, column=0)
    box_51.grid(row=5, column=1)
    box_52.grid(row=5, column=2)
    box_53.grid(row=5, column=3)
    box_54.grid(row=5, column=4)
    box_55.grid(row=5, column=5)
    box_56.grid(row=5, column=6)
    box_57.grid(row=5, column=7)
    box_58.grid(row=5, column=8)
    box_60.grid(row=6, column=0)
    box_61.grid(row=6, column=1)
    box_62.grid(row=6, column=2)
    box_63.grid(row=6, column=3)
    box_64.grid(row=6, column=4)
    box_65.grid(row=6, column=5)
    box_66.grid(row=6, column=6)
    box_67.grid(row=6, column=7)
    box_68.grid(row=6, column=8)
    box_70.grid(row=7, column=0)
    box_71.grid(row=7, column=1)
    box_72.grid(row=7, column=2)
    box_73.grid(row=7, column=3)
    box_74.grid(row=7, column=4)
    box_75.grid(row=7, column=5)
    box_76.grid(row=7, column=6)
    box_77.grid(row=7, column=7)
    box_78.grid(row=7, column=8)
    box_80.grid(row=8, column=0)
    box_81.grid(row=8, column=1)
    box_82.grid(row=8, column=2)
    box_83.grid(row=8, column=3)
    box_84.grid(row=8, column=4)
    box_85.grid(row=8, column=5)
    box_86.grid(row=8, column=6)
    box_87.grid(row=8, column=7)
    box_88.grid(row=8, column=8)
    blank.grid(row=9, column=0)
    num_0.grid(row=10, column=0)
    num_1.grid(row=10, column=1)
    num_2.grid(row=10, column=2)
    num_3.grid(row=10, column=3)
    num_4.grid(row=10, column=4)
    num_5.grid(row=10, column=5)
    num_6.grid(row=10, column=6)
    num_7.grid(row=10, column=7)
    num_8.grid(row=10, column=8)
build_board_display()
root.mainloop()
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
#Add in option for user to input they're own puzzle
#nswer = input("Do you want to use your own puzzle? (y,n): ")
#f answer == "y":
#   for i in range(len(board)):
#       nums = input("Enter the numbers for row " + str(i+1) + " seperated by a comma.\nUse zero for blank spaces. (1,0,3,0,0,6,0,0,9): ")
#       numsArr =  nums.split(",")
#       while len(numsArr) != len(board[0]):
#           print("Seems like you inputted something incorrectly, try again.")
#           nums = input("Enter the numbers for row " + str(i+1) + " seperated by a comma.\nUse zero for blank spaces. (1,0,3,0,0,6,0,0,9): ")
#           numsArr =  nums.split(",")
#       for j in range(len(board[0])):
#           while int(numsArr[j]) > 9 or int(numsArr[j]) < 0:
#               print("Seems like you inputted something incorrectly, try again.")
#               num = input("What number did you want in row " + str(i+1) + " and column + " + str(j+1) + "? ")
#               numsArr[j] = num
#           board[i][j] = int(numsArr[j].strip())

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