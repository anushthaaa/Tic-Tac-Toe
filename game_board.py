class GameBoard:
    @staticmethod
    def printGameBoard(gameBoard):
        print("\n+---+---+---+")
        for row in range(3):
            print("|", end="")
            for col in range(3):
                print(f" {gameBoard[row][col]} |", end="")
            print("\n+---+---+---+")