#will do brute force, yes start from every point and checking if word matches ele return
#will need backtracking for visited node, see once we do start from (0,0) then visited will be marked for that start point right better backtrack that step after you done with one branch for others. clean the shit ma and thats a big algo time it is. O(r*c) then dfs for every r*c
#dfs = have max depth of len(word) and four calls so = 4^len(word)
#total = O(r*c*4^len(word)) #Bruh HUGE
r, c = len(board), len(board[0])
vis = set()
def dfs(i, j, ind):
if ind == len(word):
return True
if i<0 or j<0 or i>=r or j>=c or board[i][j]!=word[ind] or (i,j) in vis:
return False
vis.add((i,j))
res = dfs(i+1, j, ind+1) or dfs(i, j+1, ind+1) or dfs(i-1, j, ind+1) or dfs(i, j-1, ind+1)
vis.remove((i,j))        #backtrack
return res
for i in range(r):
for j in range(c):
if dfs(i, j, 0):
return True
return False