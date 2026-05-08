class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # these tell us which rows and columns need to be filled with zeros 
        rows = [None] * len(matrix) 
        cols = [None] * len(matrix[0]) 

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    rows[r] = 0
                    cols[c] = 0
        
        for r in range(len(rows)):
            if rows[r] == 0:
                for i in range(len(matrix[0])):
                    matrix[r][i] = 0
        
        for c in range(len(cols)):
            if cols[c] == 0:
                for j in range(len(matrix)):
                    matrix[j][c] = 0


