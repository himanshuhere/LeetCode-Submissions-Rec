class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if not n:
            return []
        
        res = [[0]*n for _ in range(n)]
        l, r, t, d, num = 0, n-1, 0, n-1, 1
        
        while l <= r and t <= d:
            for i in range(l, r+1):
                res[t][i] = num 
                num += 1
            t += 1
            
            for i in range(t, d+1):
                res[i][r] = num
                num += 1
            r -= 1
            
            for i in range(r, l-1, -1):
                res[d][i] = num
                num += 1
            d -= 1
            
            for i in range(d, t-1, -1):
                res[i][l] = num
                num += 1
            l += 1
            
        return res