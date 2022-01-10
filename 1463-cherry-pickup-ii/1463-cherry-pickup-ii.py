class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        self.memo = {}
        return max(self.dfs(grid,0,0,0,n - 1), 0)
    
    def dfs(self,grid,i1,j1,i2,j2):
        if (i1,j1,i2,j2) in self.memo: return self.memo[(i1,j1,i2,j2)]
        
        m, n = len(grid), len(grid[0])
        #end cases
        
        if j1 == n or j2 == n or j1 == -1 or j2 == -1: return -float('inf')
        if i1 == m and i2 == m: return 0
        
        if i1 == i2 and j1 == j2:
            res = grid[i1][j1]
        else:
            res = grid[i1][j1] + grid[i2][j2]
            
        # 9 different next steps
        d1 = self.dfs(grid,i1 + 1,j1 - 1,i2 + 1,j2 - 1)
        d2 = self.dfs(grid,i1 + 1,j1 - 1,i2 + 1,j2)
        d3 = self.dfs(grid,i1 + 1,j1 - 1,i2 + 1,j2 + 1)
        d4 = self.dfs(grid,i1 + 1,j1 ,i2 + 1,j2 - 1)
        d5 = self.dfs(grid,i1 + 1,j1 ,i2 + 1,j2)
        d6 = self.dfs(grid,i1 + 1,j1 ,i2 + 1,j2 + 1)
        d7 = self.dfs(grid,i1 + 1,j1 + 1 ,i2 + 1,j2 - 1)
        d8 = self.dfs(grid,i1 + 1,j1 + 1,i2 + 1,j2)
        d9 = self.dfs(grid,i1 + 1,j1 + 1,i2 + 1,j2 + 1)
        max_res = max([d1,d2,d3,d4,d5,d6,d7,d8,d9])
        
        #if two robots step on same place
        
        self.memo[(i1,j1,i2,j2)] = max_res + res
        return max_res + res