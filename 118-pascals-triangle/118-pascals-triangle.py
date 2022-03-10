class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        #simple
        n = numRows
        pas = [[1]*(i+1) for i in range(n)]
        
        for i in range(n):
            for j in range(1, i):
                pas[i][j] = pas[i-1][j-1] + pas[i-1][j]
        
        return pas
        
        
       
    #2
    # dynamic programming bcz in every iteration we r creating new row based on prev row
        
        if numRows == 0: return []
        elif numRows == 1: return [[1]]
        
        #isme pascal triangle return karna hai to think arr of arr, else sirf operate karna hota last row pe toh hum dp jese pre and cur concept use karte
        PasTri = [[1]]
        
        for i in range(1, numRows):
            row = []
            row.append(1)   #first ele wud be 1, thus start col loop with 1 till i
            
            for j in range(1, i):
                row.append(PasTri[i-1][j-1] + PasTri[i-1][j])
            
            row.append(1)   #last ele wud also b 1 only
            PasTri.append(row)
        return PasTri
            
# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1
            