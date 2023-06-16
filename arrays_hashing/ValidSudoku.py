from collections import defaultdict

def isValidSudoku(self, board: list[list[str]]) -> bool:
        _board = defaultdict(list)
        for row_index, row in enumerate(board):
            for col_index, num in enumerate(row):
                curr_box = (row_index // 3, col_index // 3)
                if num != '.':
                        if _board[num]:
                            for (prev_row, prev_col) in _board[num]:
                                row_invalid = row_index == prev_row
                                col_invalid = col_index == prev_col
                                box_invalid = curr_box == (prev_row // 3, prev_col // 3)
                                if row_invalid or col_invalid or box_invalid:
                                    return False
                        _board[num].append((row_index,  col_index))
        return True