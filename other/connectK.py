from collections import defaultdict
from collections import Counter

class board:
    def __init__(self, k) -> None:
        self.board = defaultdict(list)
        self.win_leng = k
        
    def _checkVertWin(self, player: str, loc: int):
        column = self.board[loc]
        win_leng = self.win_leng
        if len(column) > win_leng:
            return None
        for prev_player in column[len(column) - win_leng:]:
            if prev_player != player:
                return None
        return player
    
    def _checkHorWin(self, player: str, loc: int):
        board = self.board
        win_leng = self.win_leng
        possible_columns = []
        for col in range(-(win_leng - 1), win_leng):
            possible_columns.append(board[loc + col])
            
        for row in zip(*possible_columns):
            player_count = Counter(row)
            if player_count[player] >= win_leng:
                return player
        return None
        
    def move(self, player:str, loc:int):
        column = self.board[loc]
        column.append(player)
        
        vertical_win = self._checkVertWin(player, loc)
        if vertical_win:
            return vertical_win
        
        horizontal_win = self._checkHorWin(player, loc)
        if horizontal_win:
            return horizontal_win

    