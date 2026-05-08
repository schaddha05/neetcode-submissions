class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        l = 0 
        h = len(matrix) - 1

        while l <= h:
            mid = (h + l) // 2

            if matrix[mid][n-1] >= target and matrix[mid][0] <= target:
                # found row, do binary search on row 
                low = 0 
                high = n - 1
                while low <= high:
                    m = (high + low) // 2
                    if matrix[mid][m] == target:
                        return True 
                    elif matrix[mid][m] > target:
                        high = m - 1
                    else:
                        low = m + 1
                
                return False 
            elif matrix[mid][n-1] < target: # move one row down to bigger values
                l = mid + 1 
            else:
                h = mid - 1 
            
        return False