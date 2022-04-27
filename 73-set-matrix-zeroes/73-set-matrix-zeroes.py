class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        #see notes
        R = len(matrix)
        C = len(matrix[0])
        
        #we ll use first row and first col as sign and special case we need to handle is for first row and first col sice we ll update that thus use two flags maybe
        
        frow, fcol = False, False
        for i in range(R):
            for j in range(C):
                if matrix[i][j] == 0:
                    matrix[0][j] = matrix[i][0] = 0
                    if i == 0:
                        frow = True
                    if j == 0:    
                        fcol = True
        
        
        for i in range(1, R):
            if matrix[i][0] == 0:
                for j in range(1, C):
                    matrix[i][j] = 0
        
        for j in range(1, C):
            if matrix[0][j] == 0:
                for i in range(1, R):
                    matrix[i][j] = 0
        
        if frow:
            for j in range(C):
                matrix[0][j] = 0
        if fcol:
            for i in range(R):
                matrix[i][0] = 0
     