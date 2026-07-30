class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def dfs(r, c, path):
            if ''.join(path) == word:
                return True 
            
            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]) or board[r][c] == '#':
                return False 
            
            temp = board[r][c]
            board[r][c] = '#'
            path.append(temp)
            left = dfs(r, c - 1, path)
            right = dfs(r, c + 1, path)
            up = dfs(r - 1, c, path)
            down = dfs(r + 1, c, path)
            
            board[r][c] = temp
            path.pop()

            return left or right or up or down 
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(r, c, []):
                    return True 
        
        return False 