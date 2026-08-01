class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        posDiag = set()
        negDiag = set()
        res = []
        board = [['.'] * n for _ in range(n)]
        print(board)
        def dfs(r):
            if r >= n:#found a valid solution since we iterated through each row
                res.append([''.join(row) for row in board])
                return 
            
            for c in range(n):
                if c in cols or (r + c) in posDiag or (r - c) in negDiag:
                    continue # cannot place queen at board[r][c], try next column
                
                cols.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                board[r][c] = 'Q'
                dfs(r+1)

                cols.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                board[r][c] = '.'

        dfs(0)
        return res



        