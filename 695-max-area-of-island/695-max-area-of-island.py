class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def dfs(i, j):
            nonlocal c
            if i<0 or j<0 or i>=m or j>=n or grid[i][j]==0:
                return 
            c += 1
            grid[i][j] = 0
            for x, y in (-1, 0), (1, 0), (0, -1), (0, 1):
                dfs(i+x, j+y)
        
        c = 0
        m, n = len(grid), len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    c = 0
                    dfs(i, j)
                    res = max(res, c)
        return res
                    