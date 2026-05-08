class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefixSums = []
        for r in range(len(matrix)):
            rowTotal = 0 
            curRow = []
            for c in range(len(matrix[0])):
                rowTotal += matrix[r][c]
                curRow.append(rowTotal) 
            self.prefixSums.append(curRow)
                

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0 
        
        for r in range(row1, row2 + 1):
            preRight = self.prefixSums[r][col2]
            preLeft = self.prefixSums[r][col1-1] if col1 > 0 else 0 
            res += preRight - preLeft 

        return res
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)