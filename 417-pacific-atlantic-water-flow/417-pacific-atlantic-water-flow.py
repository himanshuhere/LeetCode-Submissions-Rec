class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #will start from top and bottom and left and right, and keep checking opp condition and will fill two sets for two ocean. Intersectiong on thosetwo will be our ans
        #In a naive approach, we would have to consider each cell and find if it is reachable to both the oceans by checking if it is able to reach - 1. top or left edge(atlantic) and, 2. bottom or right edge (pacific). This would take about O((mn)^2), which is not efficient.
        r, c = len(heights), len(heights[0])
        
        def dfs(i, j, vis, prev):
            if i<0 or j<0 or i>=r or j>=c or (i,j) in vis:
                return
            if heights[i][j] < prev:
                return
            
            vis.add((i,j))
            dfs(i+1, j, vis, heights[i][j])
            dfs(i, j+1, vis, heights[i][j])
            dfs(i-1, j, vis, heights[i][j])
            dfs(i, j-1, vis, heights[i][j])
        
        pac, atl = set(), set()
        
        #row
        for j in range(c):
            dfs(0, j, pac, heights[0][j])
            dfs(r-1, j, atl, heights[r-1][j])
        
        #col
        for i in range(r):
            dfs(i, 0, pac, heights[i][0])
            dfs(i, c-1, atl, heights[i][c-1])
        
        #now intersection
        res = []
        for i in range(r):
            for j in range(c):
                if (i,j) in pac and (i,j) in atl:
                    res.append((i,j))
        return res
            