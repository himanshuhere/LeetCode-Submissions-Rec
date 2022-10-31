class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # clockwise rotate
        # first reverse up to down, then swap the symmetry
        # 1 2 3         7 8 9       7 4 1
        # 4 5 6     =>  4 5 6   =>  8 5 2
        # 7 8 9         1 2 3       9 6 3
        
        # matrix.reverse()
        #in place
        #reverese
        i = 0
        j = len(matrix)-1
        while i < j:
            for k in range(len(matrix[0])):
                matrix[i][k], matrix[j][k] = matrix[j][k], matrix[i][k]
            i += 1
            j -= 1
            
        #transpose
        for i in range(len(matrix)):
            for j in range(i, len(matrix[0])):      #range(i+1, len(matrix[0]))
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]