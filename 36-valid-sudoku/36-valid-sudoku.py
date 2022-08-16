class Solution:
    def isValidSudoku(self, A: List[List[str]]) -> bool:
        #o(n^2), o(n)
        row=set()   #name this set generic any
        
        for i in range(len(A)):
            for j in range(len(A[0])):
                curr = A[i][j]
                if(curr!='.'):
                    
                    r = ('r', i, curr)  #create 3 set for each or maybe do like this 'r', 'c' etc
                    c = ('c', j, curr)
                    b = ('b', i//3, j//3, curr)
                    
                    if r in row or c in row or b in row:
                        return False
                    
                    row.add(r)
                    row.add(c)
                    row.add(b)
                    
        return True