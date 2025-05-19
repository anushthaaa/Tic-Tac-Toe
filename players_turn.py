class Player:
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