class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        res = []
        for i in range(len(matrix[0])):
            temp = []
            for j in range(len(matrix)):
                temp.append(matrix[j][i])
            res.append(temp)
        return res
    
    
        # return zip(*matrix)
        
        #return [[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]