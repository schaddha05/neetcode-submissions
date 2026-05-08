class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        negDiag = set() # (r-c)
        posDiag = set() # (r+c)

        board = [['.'] * n for i in range(n)]
        res = []
        def dfs(r):
            if r == n:
                copy = [''.join(row) for row in board]
                res.append(copy)
                return 

            # try every column in current row
            for c in range(n):
                if c in col or (r+c) in posDiag or (r-c) in negDiag:
                    continue 

                col.add(c) 
                negDiag.add(r-c)
                posDiag.add(r+c)
                board[r][c] = 'Q'
                dfs(r+1)

                col.remove(c) 
                negDiag.remove(r-c)
                posDiag.remove(r+c)
                board[r][c] = '.'

        dfs(0)
        return res  