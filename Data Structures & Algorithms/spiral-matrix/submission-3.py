class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top = 0
        bottom = len(matrix) - 1 
        l = 0 
        r = len(matrix[0]) -1 

        res = [] 

        while l <= r and top <= bottom:
            # top row 
            for i in range(l, r + 1):
                res.append(matrix[top][i])

            # right column
            for i in range(top + 1, bottom + 1):
                res.append(matrix[i][r])
            
            if top < bottom: 
                # bottom row 
                for i in range(r-1, l-1, -1):
                    res.append(matrix[bottom][i])
            
            if l < r: 
                # left column
                for i in range(bottom-1, top, -1):
                    res.append(matrix[i][l])
            
            l += 1
            r -= 1
            top += 1
            bottom -= 1
        
        return res