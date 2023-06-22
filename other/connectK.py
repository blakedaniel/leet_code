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
        
        left_index = 0
        final_index = len(possible_columns) - 1
        right_index = min(win_leng - 1, final_index)
        
        while right_index <= final_index:
            curr_columns = possible_columns[left_index:right_index + 1]
            
            for row in zip(*curr_columns):
                player_count = {}
                curr_player = None
                
                for player in row:
                    
                    if curr_player != player:
                        curr_player = player
                        player_count[player] = 0
                    
                    player_count[player] += 1
                    player1, player2 = player_count.keys()
                    player1_win = player_count[player1] == win_leng
                    player2_win = player_count[player2] == win_leng
                    tie = (player1_win and player2_win)
                    
                    if tie:
                        return player1, player2
                    elif player1_win:
                        return player1
                    elif player2_win:
                        return player2

            left_index += 1
            right_index += 1
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

    