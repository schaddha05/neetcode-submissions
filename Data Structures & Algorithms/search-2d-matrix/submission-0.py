class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for i in range(len(matrix)):
            left = 0
            right = len(matrix[i])-1
            while left <=right:
                midpoint = (left+right)//2
                if matrix[i][midpoint] == target:
                    return True
                elif matrix[i][midpoint] > target:
                    right = midpoint - 1 
                else:
                    left = midpoint + 1
        return False    