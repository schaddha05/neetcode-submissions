class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        from collections import defaultdict
        rows = defaultdict(set)
        columns = defaultdict(set)
        squares = defaultdict(set)
        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    continue 
                else:
                    r = (row // 3) % 3
                    c =  (col // 3) % 3
                    if board[row][col] in rows[row] or board[row][col] in columns[col] or board[row][col] in squares[(r,c)]:
                        return False
                    else:
                        rows[row].add(board[row][col])
                        columns[col].add(board[row][col])
                        squares[(r,c)].add(board[row][col])

        return True 
        