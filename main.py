from random import randrange


# printing the game board
def printGameBoard(gameBoard):
    print("\n+---+---+---+")
    for row in range(3):
        print("|", end="")
        for col in range(3):
            print(f" {gameBoard[row][col]} |", end="")
        print("\n+---+---+---+")

def playerInput(gameBoard):
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
        gameBoard[row][colm] = "O" # set "O" as users inp

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
        if gameBoard[x][0] == sgn and gameBoard[x][1] == sgn and gameBoard[x][2] == sgn:
            return who
    for x in range(3):
        if gameBoard[0][x] == sgn and gameBoard[1][x] == sgn and gameBoard[2][x] == sgn:
            return who
    

    # for checking diagonals
    if gameBoard[0][0] == sgn and gameBoard[1][1] == sgn and gameBoard[2][2] == sgn:
        return who
    
    if gameBoard[0][2] == sgn and gameBoard[1][1] == sgn and gameBoard[2][0] == sgn:
        return who
    return None
        
def draw_move(gameBoard):
    """lets comp make a move"""
    free = not_occupied_space(gameBoard)
    count = len(free)

    print("Computer is choosing its position...")

    # pick one random empty cell and place "X" there
    if count > 0:
        c_move = randrange(count)
        row, colm = free[c_move]
        gameBoard[row][colm] = "X"

if __name__ == "__main__" :
    print("----WELCOME TO TIC TAC TOE---")
    print(".............................")
    print("\nYou are 'O' and the computer is 'X'\n")

    gameBoard = [[1,2,3], [4,5,6], [7,8,9]]
    free = not_occupied_space(gameBoard)
    your_turn = True
    victor = None

    printGameBoard(gameBoard)


    while len(free):
        if your_turn:
            playerInput(gameBoard)
            victor = check_victor(gameBoard, "O")

        else:
            draw_move(gameBoard)
            victor = check_victor(gameBoard, "X")

        printGameBoard(gameBoard)


        if victor != None:
            break
        
        your_turn = not your_turn
        free = not_occupied_space(gameBoard)

    if victor == "you":
        print("Congratulations, you won!")
    elif victor == "me":
        print("OOPSS...I won. Better luck next time.")
    else:
        print("IT'S A TIEEEE!")

    



        





		






