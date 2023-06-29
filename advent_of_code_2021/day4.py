
# input: first row is random numbers drawn
# input: remain rows are boards, with every new board split by empty row
# output: for first winning board, (sum of all unmarked numbers) * the winning number
# Bing is made up of a random numbers drawn and some n number of boards with some m number
# of the m boards belonging to each player
# each board is made of a 5 x 5 gride of randomly generated numbers
# number is drawn
# if number is on board, number is marked and removed from being played (replace num with X)
# if row where the most recently drawn number was marked consists of just X's (5 x's) board has won 
# if col where the most recently drawn number was marked
from collections import defaultdict
from itertools import count

class Board:
    def __init__(self, id:int, schema:dict[list]) -> None:
        self.id = id
        self.schema = schema
        self.matrix = [[0 for cnt in range(5)] for cnt in range(5)]

class Bingo:
    def __init__(self, input:str) -> None:
        self.input = input.split('\n')
        self.boards = {}
        self.winners = defaultdict(list) # {num: [board1, board2]}
        
    def set_game(self):
        boards = self.boards
        input = self.input
        self.drawn = input[0].split(',')
        
        input = input[2:]
        board_id = count()
        while len(input) != 0:
            five_rows, input = input[:5], input[6:]
            board_schema = defaultdict(list) # {num: (row, col)}
            for row, nums in enumerate(five_rows):
                nums = nums.split()
                for col, num in enumerate(nums):
                    board_schema[num].append((row, col))
            
            board = Board(board_id, board_schema)
            boards.append(board)
        
    def mark_board(self, board:Board, num:str):
        if num not in board.schema:
            return
        
        coords = board.schema[num]
        for row, col in coords:
            board.matrix[row][col] = 1
        
        del board.schema[num]
        
        return coords
        
    def check_hor_vic(self, board:Board, coords:list[tuple]):
        # horizontal win
        for coord in coords:
            row, _ = coord
            if sum(board.matrix[row]) == 5:
                return board
        
    def check_vert_vic(self, board:Board, coords:list[tuple]):
        # vertical win
        for coord in coords:
            _, col = coord
            col_sum = 0
            for row in board.matrix:
                col_sum += row[col]
            if col_sum == 5:
                return board
    
    # def check_first_winner(self, num:str):
    #     boards = self.boards
    #     for board in boards:
    #         coords = self.mark_board(board, num)
    #         if not coords:
    #             continue
    #         hor = self.check_hor_vic(board, coords)
    #         ver = self.check_vert_vic(board, coords)
    #         if hor or ver:
    #             return board

    def check_winners(self, num:str):
        boards = self.boards
        winners = self.winners
        remove_idx = []
        for idx, board in enumerate(boards):
            coords = self.mark_board(board, num)
            if not coords:
                continue
            hor = self.check_hor_vic(board, coords)
            ver = self.check_vert_vic(board, coords)
            if hor or ver:
                winners[num].append(board)
                remove_idx.append(idx)
        return remove_idx
        

            
    def final_score(self, win_board:Board, win_num:str):
        win_num = int(win_num)
        win_sum = 0
        for num in win_board.schema:
            win_sum += int(num)
        return win_sum * win_num
            

input = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""

# def main():
#     bingo = Bingo(input)
#     bingo.set_game()
#     drawn = bingo.drawn

#     for num in drawn:
#         board = bingo.check_first_winner(num)
        
#         if board:
#             return bingo.final_score(board, num)

def main():
    bingo = Bingo(input)
    bingo.set_game()
    drawn = bingo.drawn
    winners = bingo.winners
    last_winning_num = None

    for num in drawn:
        winner_idxs = bingo.check_winners(num)
        for idx in winner_idxs:
            last_winning_num = num
            bingo.boards.pop(idx)
    
    final_winning_board = winners[last_winning_num][0]
    breakpoint()
    return bingo.final_score(final_winning_board, last_winning_num)

print(main())