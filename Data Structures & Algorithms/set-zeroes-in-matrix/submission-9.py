class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])
        rows = [None] *  m
        cols = [None] * n

        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    rows[r] = 0
                    cols[c] = 0
        
        for r in range(m):
            if rows[r] == 0:
                for c in range(n):
                    matrix[r][c] = 0
        
        for c in range(n):
            if cols[c] == 0 :
                for r in range(m):
                    matrix[r][c] = 0 
    
        