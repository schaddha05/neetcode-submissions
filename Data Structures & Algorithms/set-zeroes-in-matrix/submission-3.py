class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])
        dup = [[matrix[r][c] for c in range(n)] for r in range(m)]

        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    # set row to 0 
                    for i in range(n):
                        dup[r][i] = 0
                    # set col to 0 
                    for j in range(m):
                        dup[j][c] = 0 
        
        for r in range(m):
            for c in range(n):
                matrix[r][c] = dup[r][c]
        