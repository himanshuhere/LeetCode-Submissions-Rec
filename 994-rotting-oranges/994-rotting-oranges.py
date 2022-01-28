class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #Multi source BFS - Classic Problem
        #whle q is empty that is good, but what is there is one or some fresh oranges were there and since they were not diretly connnected neighbours we cant catch them in queue and process, thats y fresh count will help at last. see the code
        R, C = len(grid), len(grid[0])
        time, fresh = 0, 0
        q = deque()
        
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append([i,j])
        
        dir = [[1,0], [0,1], [-1,0], [0,-1]]
        #Bfs multi source
        while q and fresh:          #either queue else fresh, one sould be present
            for _ in range(len(q)):
                r, c = q.popleft()
                
                for dx, dy in dir:
                    nr, nc = r+dx, c+dy
                    
                    if nr<0 or nr==R or nc<0 or nc==C or grid[nr][nc] != 1:
                        continue
                    grid[nr][nc] = 2            #MOST IMP STEP, else TLE
                    q.append([nr, nc])
                    fresh -= 1
            time += 1

        return time if fresh == 0 else -1
                