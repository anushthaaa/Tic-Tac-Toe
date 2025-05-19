from game_board import GameBoard
from computers_turn import Computer
from players_turn import Player
from victory import Victory
from occupied_space import CheckOccupiedSpace


def main():
    print("----WELCOME TO TIC TAC TOE---")
    print(".............................")
    print("\nYou are 'O' and the computer is 'X'\n")

    gameBoard = [[1,2,3], [4,5,6], [7,8,9]]
    free = CheckOccupiedSpace.not_occupied_space(gameBoard)
    your_turn = True
    victor = None

    GameBoard.printGameBoard(gameBoard)


    while len(free):
        if your_turn:
            Player.playerInput(gameBoard)
            victor = Victory.check_victor(gameBoard, "O")

        else:
            Computer.draw_move(gameBoard, CheckOccupiedSpace.not_occupied_space)
            victor = Victory.check_victor(gameBoard, "X")

        GameBoard.printGameBoard(gameBoard)


        if victor != None:
            break
        
        your_turn = not your_turn
        free = CheckOccupiedSpace.not_occupied_space(gameBoard)

    if victor == "you":
        print("Congratulations, you won!")
    elif victor == "me":
        print("OOPSS...I won. Better luck next time.")
    else:
        print("IT'S A TIEEEE!")

if __name__ == "__main__":
    main()

    



        





		






