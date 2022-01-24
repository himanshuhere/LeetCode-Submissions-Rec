class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # consider worst case that we have single island,
        # then our peri will be 4 right, now we will use this same 
        # thing to make sol, so for every 1/island we ll add 4 to res
        # but we need to minus the shared sides, so we ll 
        # keep watching the prev index of i and j, if they got 1 then we ll 
        # minus 2 cuz two block have 8 sides, will share 1 wall twice so 
        # remove 2.
        # res = 0
        # for i in range(len(grid)):
        #     for j in range(len(grid[0])):
        #         if grid[i][j] == 1:
        #             res += 4
        #             if i > 0 and grid[i-1][j] == 1: res -= 2   #neighbour
        #             if j > 0 and grid[i][j-1] == 1: res -= 2   #neighbour
        # return res
        
        #2
        #same time o(m*n) intuitive also i have thats dfs. so where is permiter contri, on out of bounds and on water layers. we just need to enter once in any island 1 then see the also
        
        def dfs(i, j):
            if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]==0:
                return 1
            if grid[i][j]==-1:  #dont go back, better use DS for interview wont cha
                return 0
            
            grid[i][j] = -1
            perim = dfs(i+1, j) + dfs(i, j+1) + dfs(i-1, j) + dfs(i, j-1)
            return perim
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    return dfs(i,j)
        
