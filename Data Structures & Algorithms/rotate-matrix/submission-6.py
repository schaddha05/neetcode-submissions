class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l = 0 
        r = len(matrix[0]) -1 
        
        while l <= r:
            for i in range(r - l):
                u, b = l, r
                topLeft = matrix[u][l + i]
                matrix[u][l + i] = matrix[b - i][l] 
                matrix[b - i][l] = matrix[b][r - i]
                matrix[b][r - i] = matrix[u + i][r]
                matrix[u + i][r] = topLeft 
            
            l += 1 
            r -= 1
           