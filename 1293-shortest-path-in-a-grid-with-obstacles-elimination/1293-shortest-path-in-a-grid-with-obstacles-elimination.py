class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        #TC m*n*k, as k is also one factor here to add some nodes again 
        
        m, n = len(grid), len(grid[0])
        q = collections.deque([[0, 0, 0]])    # row, col, num of obstables met so far
        visited = {(0, 0): 0}                 # row, col   =>   num of obstables met so far
        steps = 0
        
        while q:
            size = len(q)
            for _ in range(size):
                r, c, obs = q.popleft()
                
                if obs > k: 
                    continue           
                if r == m - 1 and c == n - 1: 
                    return steps
                
                for r2, c2 in [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]:
                    if 0 <= r2 < m and 0 <= c2 < n:
                        next_obs = obs + 1 if grid[r2][c2] == 1 else obs
                        
                        if (r2, c2) not in visited or next_obs < visited[(r2, c2)]:
                            visited[(r2, c2)] = next_obs
                            q.append([r2, c2, next_obs])
            steps += 1
        return -1
    
    
    #we are checking, if first time i, j visit keep going with counting obstacles. If again visit pls check if this path having less obstacles than the previous path that we would have in visited, if yes chose this one and update visited.
    #You see if we reach at end we ll return, if we havent reach end and sath me have crossed obstacle limit too then stop that path, how? CONTINUE
    #diff than classic matrix bfs: wha visited use to ignore the revisit, yaha bhi same if this revisit is costly or same, if cheaper (in obstacle sense), better conside this untill we get more cheaper. 