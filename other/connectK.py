from collections import defaultdict
from itertools import zip_longest

class board:
    def __init__(self, k) -> None:
        self.board = defaultdict(list)
        self.win_leng = k
        self.players = ('red', 'blue')
        
    def _checkVertWin(self, player: str, loc: int):
        column = self.board[loc]
        win_leng = self.win_leng
        
        if len(column) > win_leng:
            return None
        
        for prev_player in column[:win_leng]:
            if prev_player != player:
                return None
        return player
    
    def _checkHorWin(self, player: str, loc: int):
        board = self.board
        win_leng = self.win_leng
        players = self.players
        win_cases = {}
        possible_columns = []
        
        for player in players:
            win_cases[player] = (player for player in range(win_leng))
            
        for col in range(-(win_leng - 1), win_leng):
            possible_columns.append(board[loc + col])
            
        for row in zip_longest(*possible_columns):
            
            player1, player2 = players
            player1_win = win_cases[player1] in row
            player2_win = win_cases[player2] in row
            tie = player1_win and player2_win
            
            if tie:
                return player1, player2
            elif player1_win:
                return player1
            elif player2_win:
                return player2
        return None
        
    def move(self, player:str, loc:int):
        column = self.board[loc]
        column.insert(0, player)
        
        vertical_win = self._checkVertWin(player, loc)
        if vertical_win:
            return vertical_win
        
        horizontal_win = self._checkHorWin(player, loc)
        if horizontal_win:
            return horizontal_win

    