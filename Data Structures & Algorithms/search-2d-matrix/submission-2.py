class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start = 0 
        end = len(matrix)-1 

        while start <= end: 
            mid = (end + start) // 2
            if target >= matrix[mid][0] and target <= matrix[mid][len(matrix[mid])-1]:
                start = 0 
                end = len(matrix[0]) -1
                while start <= end:
                    mid2 = (end + start) // 2
                    if matrix[mid][mid2] == target:
                        return True 
                    elif target < matrix[mid][mid2]:
                        end = mid2 - 1
                    else:
                        start = mid2 + 1 
            elif target < matrix[mid][0]:
                end = mid - 1 
            elif target > matrix[mid][len(matrix[mid])-1]:
                start = mid + 1 

        return False 