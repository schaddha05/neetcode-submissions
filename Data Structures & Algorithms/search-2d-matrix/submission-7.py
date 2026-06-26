class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix) # rows
        n = len(matrix[0]) # columns

        l = 0
        r = m - 1

        while l <= r:
            mid = (r + l) // 2

            if target <= matrix[mid][n-1] and target >= matrix[mid][0]:
                low = 0 
                high = n - 1
                while low <= high:
                    middle = (low + high) // 2

                    if matrix[mid][middle] == target:
                        return True
                    elif target > matrix[mid][middle]:
                        low = middle + 1 
                    else:
                        high = middle - 1 
                
                return False
            elif target > matrix[mid][n-1]:
                l = mid + 1 
            elif target < matrix[mid][0]:
                r = mid - 1
        
        return False
