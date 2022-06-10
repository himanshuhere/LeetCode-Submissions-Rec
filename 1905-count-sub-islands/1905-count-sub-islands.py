class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        #idea
        #first remove the sub island which is there in 2 but not in 1
        #second - after first we ll have valid 1s in grid2, now count them
        #we ll use same dfs function, where instead visisted we ll use changing i,j pos value and that will help in removing invalid sub island too see
        
        m=len(grid1)
        n=len(grid1[0])

        def dfs(i,j):
            if i<0 or i>=m or j<0 or j>=n or grid2[i][j]==0:
                return

            grid2[i][j] = 0
            dfs(i+1,j)
            dfs(i,j+1)
            dfs(i,j-1)
            dfs(i-1,j)

        # removing all the non-common sub-islands
        for i in range(m):
            for j in range(n):
                if grid1[i][j]==0 and grid2[i][j]==1:
                    dfs(i,j)

        c=0
        # counting sub-islands
        for i in range(m):
            for j in range(n):
                if grid2[i][j]==1:
                    dfs(i,j)
                    c+=1
        return c