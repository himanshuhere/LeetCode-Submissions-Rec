class Solution:
    def longestIncreasingPath(self, mat: List[List[int]]) -> int:
        R, C = len(mat), len(mat[0])
        
        @lru_cache(None)            #this dp memoization will save time
        def dfs(i, j, prev):
            if i<0 or i>=R or j<0 or j>=C or mat[i][j] <= prev:
                return 0
            
            res = 1 + max(dfs(i+1, j, mat[i][j]), dfs(i, j+1, mat[i][j]), dfs(i-1, j, mat[i][j]), dfs(i, j-1, mat[i][j]))
            return res
        
        
        res = -math.inf
        for i in range(R):
            for j in range(C):
                res = max(res, dfs(i,j,-1))
        
        return res