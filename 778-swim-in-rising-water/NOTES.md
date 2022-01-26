#neetcode, can do dfs but since we can easily do modified bfs thats better and clear. Instead operating heap on cost, we ll operate of max time/height we have covered for this path we are in
N = len(grid)
dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]
minH = [[grid[0][0], 0, 0]]     #start time, r, c
vis = set()
while minH:
t, r, c = heapq.heappop(minH)
if r == N-1 and c == N-1:
return t
for dx, dy in dir:
newc, newr = r+dx, c+dy
if newc < 0 or newc == N or newr < 0 or newr == N or (newr, newc) in vis:
continue
vis.add((newr, newc))
heapq.heappush(minH, [max(t, grid[newr][newc]), newr, newc])