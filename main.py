from random import randrange


# printing the game board
def printGameBoard(gameBoard):
    print("\n+---+---+---+")
    for row in range(3):
        print("|", end="")
        for col in range(3):
            print(f" {gameBoard[row][col]} |", end="")
        print("\n+---+---+---+")

def playerinput(gameBoard):
    ok = False
    while not ok:
        move = input("Enter your move: ")
        ok = len(move) == 1 and move >= '1' and move <= '9' # is user's input valid?
        if not ok:
            print("Bad move - repeat your input!") # no, it isn't - do the input again
            continue
        move = int(move) - 1 	# cell's number from 0 to 8
        # convert the input into row and column
        row = move // 3
        colm = move % 3
        sign = gameBoard[row][colm] # check the selected sq
        ok = sign not in ["O", "X"]
        if not ok: # already occupied
            print("Field is already occupied- repeat your input.")
            continue
    sign = "O" # set "O" as users inp

def not_occupied_space(gameBoard):
    free = []
    for x in range(3):
        for y in range(3):
            if gameBoard[x][y] not in ["O", "X"]: # is this cell free?
                free.append((x,y)) # if yes, add new tuple to the free[] list

    return free

def check_victor(gameBoard, sgn):
    """checks if 'O' or 'X' has won the game."""
    if sgn == "X":
        who = "me"
    elif sgn == "O":
        who = "you"

    # checks rows com 

    for x in range(3):
        if gameBoard[x][0] == sgn and gameBoard[x][1] and gameBoard[x][2] == sgn:
            return who
        if gameBoard[0][x] == sgn and gameBoard[1][x] and gameBoard[2][x] == sgn:
            return who
        # checks diagnols
    if gameBoard[x][x] != sgn:
        cross1 = False
    if gameBoard[2-x][2-x] != sgn:
        cross2 = False

    return None
        
def draw_move(gameBoard):
    """lets comp make a move"""
    free = not_occupied_space(gameBoard)
    count = len(free)

    # pick one random empty cell and place "X" there
    if count > 0:
        c_move = randrange(count)
        row, colm = free[c_move]
        gameBoard[row][colm] = "X"

if __name__ == "__main__" :
    print("----WELCOME TO TOC TAC TOE---")
    print(".............................")

    gameBoard = [[1,2,3], [4,5,6], [7,8,9]]
    printGameBoard(gameBoard)
    free = not_occupied_space(gameBoard)
    your_turn = True
    victor = None

    while len(free):
        printGameBoard(gameBoard)
        if your_turn:
            playerinput(gameBoard)
            victor = check_victor(gameBoard, "O")

        else:
            draw_move(gameBoard)
            victor = check_victor(gameBoard, "X")

        if victor != None:
            break
        
        your_turn = not your_turn
        free = not_occupied_space(gameBoard)

    printGameBoard(gameBoard)
    if victor == "you":
        print("You won!")
    elif victor == "me":
        print("I won")
    else:
        print("Tie!")

    



        





		






