class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n = len(board)
        m = len(board[0])

        def dfs(r,c):
            if r not in range(n) or c not in range(m) or board[r][c] != 'O':
                return 
            
            board[r][c] = '#'
            dfs(r, c+1)
            dfs(r, c-1)
            dfs(r+1, c)
            dfs(r-1, c)


        # rows
        for c in range(m):
            if board[0][c] == 'O':
                dfs(0, c) 
            if board[n-1][c] == 'O':
                dfs(n-1, c)
        
        # columns
        for r in range(n):
            if board[r][0] == 'O':
                dfs(r, 0)
            if board[r][m-1] == 'O':
                dfs(r, m-1)
        

        for r in range(n):
            for c in range(m):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == '#':
                    board[r][c] = 'O'