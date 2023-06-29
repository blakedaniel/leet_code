
class Boat:
    def __init__(self, loc:tuple[tuple]=((0,0))) -> None:
        # ((0, 1), (0, 2))
        self.id = len(self.loc)
        self.loc = {(row, col) for row,col in loc}
        

class Player:
    def __init__(self, id:int, rows:int=5, cols:int=5) -> None:
        # what are the options for each location on the map?
        ## boat no hit
        ## boat hit
        ## no boat hit
        self.id = id
        self.board = [[0 for col in cols] for row in rows]
        self.boats = set()
        
    def place_boat(self, loc:tuple[tuple]):
        # loc: ((0, 1), (0, 2))
        board = self.board
        boats = self.boats
        boat = Boat(loc)
        for col, row in loc:
            board[row][col] = boat
        boats.add(boat)
    
    def guess_boat(self, loc:tuple[tuple]):
        row = loc[0]
        col = loc[1]
        boat = self._check_hit(col, row)
        sunk = self._check_sunk(boat)
        vic = self._check_vic
        if boat and sunk:
            return vic        
        
    # check_hit
    def _check_hit(self, col:int, row:int):
        board = self.board
        if board[row][col] == 1:
            raise ValueError
        elif board[row][col].isinstance(Boat):
            boat = board[row][col]
            boat.loc.remove((col, row))
            return boat
        elif board[row][col] == 0:
            board[row][col] = 1
            return None

    # check_sunk
    def _check_sunk(self, boat:Boat):
        boats = self.boats
        board = self.board
        if len(boat.loc) != 0:
            return
        
        boats.remove(boat)
        for col, row in boat.loc:
            board[row][col] = 1
        return 1

    # check_victory
    def _check_vic(self):
        boats = self.boats
        id = self.id
        if len(boats) == 0:
            return (id, 0)
        
    
        