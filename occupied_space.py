
class CheckOccupiedSpace():
    def not_occupied_space(gameBoard):
        free = []
        for x in range(3):
            for y in range(3):
                if gameBoard[x][y] not in ["O", "X"]: # is this cell free?
                    free.append((x,y)) # if yes, add new tuple to the free[] list

        return free