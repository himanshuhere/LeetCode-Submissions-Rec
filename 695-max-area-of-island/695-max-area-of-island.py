class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(i,j):
    
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]) or grid[i][j] == 0:
                return 0

            grid[i][j] = 0

            return 1 + dfs(i,j+1)+dfs(i,j-1)+dfs(i-1,j)+dfs(i+1,j)
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                
                if grid[i][j] == 1:
                    count = max(dfs(i,j), count)
                    
        return count
        