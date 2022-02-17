for _ in range(len(rotten)):
x, y = rotten.popleft()
# visit all the adjacent cells
for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
# calculate the coordinates of the adjacent cell
xx, yy = x + dx, y + dy
# ignore the cell if it is out of the grid boundary
if xx < 0 or xx == rows or yy < 0 or yy == cols:
continue
# ignore the cell if it is empty '0' or visited before '2'
if grid[xx][yy] == 0 or grid[xx][yy] == 2:
continue
# update the fresh oranges count
fresh_cnt -= 1
# mark the current fresh orange as rotten
grid[xx][yy] = 2
# add the current rotten to the queue
rotten.append((xx, yy))
​
# return the number of minutes taken to make all the fresh oranges to be rotten
# return -1 if there are fresh oranges left in the grid (there were no adjacent rotten oranges to make them rotten)
return minutes_passed if fresh_cnt == 0 else -1