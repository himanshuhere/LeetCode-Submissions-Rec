class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        #row
        for i in range(1, len(matrix)):
            matrix[i][0] += matrix[i-1][0]
        
        #col
        for j in range(1, len(matrix[0])):
            matrix[0][j] += matrix[0][j-1]
        
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                matrix[i][j] += (matrix[i-1][j] + matrix[i][j-1] - matrix[i-1][j-1])            
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        matrix = self.matrix
        return matrix[row2][col2] - (matrix[row2][col1-1] if col1 > 0 else 0) - (matrix[row1-1][col2] if row1 > 0 else 0) + (matrix[row1-1][col1-1] if (row1>0 and col1>0) else 0)
    
    
    
    #Sum(ABCD) = Sum(OD)−Sum(OB)−Sum(OC)+Sum(OA)


