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