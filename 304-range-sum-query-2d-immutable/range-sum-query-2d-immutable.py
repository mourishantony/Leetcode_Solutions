class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m = len(matrix)
        n = len(matrix[0])
        mt1 = [[0] * (n + 1) for _ in range(m + 1)]
        for row in range(m):
            rowSum = 0
            for col in range(n):
                rowSum += matrix[row][col]
                mt1[row + 1][col + 1] = rowSum + mt1[row][col + 1]
        self.mt1 = mt1

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        mt = self.mt1
        return mt[row2 + 1][col2 + 1] - mt[row1][col2 + 1] - mt[row2 + 1][col1] + mt[row1][col1]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)