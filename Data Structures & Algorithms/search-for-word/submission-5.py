class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        seen = set() 
        
        def dfs(row, col, i):
            if i == len(word):

                return True 
            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] != word[i] or (row,col) in seen:
                return False 
            
            seen.add((row, col))
            found =  (dfs(row, col - 1, i + 1) or  
                    dfs(row - 1, col, i + 1) or
                    dfs(row, col + 1, i + 1) or
                    dfs(row + 1, col, i + 1))
            seen.remove((row,col))
            return found

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0] and dfs(r,c, 0):
                    return True
        
        return False 