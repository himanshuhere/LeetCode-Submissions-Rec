class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        #no DFS - when two person same time, use DP kind of DP and DFS mix see
        #pls see n understand how could you work two dfs on same space simultaneously
        #Asumption - going down (making 1 to 0) then coming up. Better go down for both and see if same place then pick once cherries else sum same thing actually
        N = len(grid)
        lookup = {}
        
        def solve(x1, y1, x2, y2):
            # check if we reached bottom right corner
            if x1 == N-1 and y1 == N-1: 
                return grid[x1][y1]
            
            # out of the grid and thorn check
            if x1 == N or y1 == N or x2 == N or y2 == N or grid[x1][y1] == -1 or grid[x2][y2] == -1: 
                return float("-inf")
            
			# memorization check
            lookup_key = (x1, y1, x2, y2)
            if lookup_key in lookup: return lookup[lookup_key]
            
			# pick your cherries
            if x1 == x2 and y1 == y2:
                cherries = grid[x1][y1]
            else:
                cherries = grid[x1][y1] + grid[x2][y2]
                
            res = cherries + max(
                solve(x1 + 1, y1, x2 + 1, y2),  # right, right
                solve(x1, y1 + 1, x2, y2 + 1),  # down, down
                solve(x1 + 1, y1, x2, y2 + 1),  # right, down
                solve(x1, y1 + 1, x2 + 1, y2), # down, right
            )
            
            lookup[lookup_key] = res
            return res
        
        res = solve(0, 0, 0, 0)
        return res if res > 0 else 0