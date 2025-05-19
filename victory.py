class Victory:
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
        