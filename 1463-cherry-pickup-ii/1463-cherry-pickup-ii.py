class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        #clean code, somethings to see. everytime three down movement thus i + 1 is constant and j is diff [-1, 0, 1]
        #second since both will be move same time at same row, they both will reach last row at same time maybe diff col but same row bcs i+1 everytime, thus we ll have three states (i, j1, j2)
        # see code
        n, m = len(grid), len(grid[0])
        
        @lru_cache(None)
        def f(i, j1, j2):
            #out of bound
            if j1 < 0 or j2 < 0 or j1 >= m or j2 >= m:
                return -math.inf
            
            #base case desitination
            if i == n-1:
                if j1 == j2:    #pick one
                    return grid[i][j1]
                else:
                    return grid[i][j1] + grid[i][j2]
            
            #explore path, for j combination= 9 paths
            maxi = -math.inf
            picked = 0
            if j1 == j2:    #pick one
                picked = grid[i][j1]
            else:
                picked = grid[i][j1] + grid[i][j2]
            
            for c1 in range(-1, 2):     #-1, 0, 1
                for c2 in range(-1, 2):
                    maxi = max(maxi, picked + f(i+1, j1+c1, j2+c2))
            return maxi
        
        return f(0, 0, m-1)