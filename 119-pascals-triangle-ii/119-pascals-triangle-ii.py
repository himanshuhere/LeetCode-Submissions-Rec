class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        
        if rowIndex == 1:
            return [1, 1]
        
        temp = self.getRow(rowIndex-1)
        
        cur = []
        cur.append(1)
        for i in range(1, len(temp)):
            cur += [temp[i-1]+temp[i]]
        cur.append(1)
        return cur
    
#         if rowIndex   == 0: return [1]
#         elif rowIndex == 1: return [1,1]
#         Tri = [[1]]
#         for i in range(1,rowIndex+1):
#             row = [1]
#             for j in range(1,i):
#                 row.append(Tri[i-1][j-1] + Tri[i-1][j]) 
#             row.append(1)
#             Tri.append(row)
#             if i == rowIndex: return row
       