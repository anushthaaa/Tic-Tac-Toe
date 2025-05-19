from random import randrange

class Computer:
    def draw_move(gameBoard, not_occupied_space):
        """lets comp make a move"""
        free = not_occupied_space(gameBoard)
        count = len(free)

        print("Computer is choosing its position...")

        # pick one random empty cell and place "X" there
        if count > 0:
            c_move = randrange(count)
            row, colm = free[c_move]
            gameBoard[row][colm] = "X"