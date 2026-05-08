class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows 
        for row in range(9):
            row_seen = set()
            for col in range(9):
                if board[row][col] != '.':
                    if board[row][col] in row_seen:
                        return False
                    else:
                        row_seen.add(board[row][col])
                else:
                    continue
        # check columns
        for col in range(9):
            col_seen = set()
            for row in range(9):
                if board[row][col] != '.':
                    if board[row][col] in col_seen:
                        return False
                    else:
                        col_seen.add(board[row][col])
                else:
                    continue
        # check squares 
        from collections import defaultdict
        seen = defaultdict(set)

        for row in range(9):
            for col in range(9):
                if board[row][col] != '.':
                    r = (row // 3) % 3
                    c =  (col // 3) % 3
                    if board[row][col] in seen[(r,c)]:
                        return False
                    else:
                        seen[(r,c)].add(board[row][col])
                else:
                    continue
        return True 

       