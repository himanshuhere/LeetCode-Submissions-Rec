class Solution:
    def knightProbability(self, n: int, K: int, row: int, column: int) -> float:
        dx = [-2,-1,1,2,2,1,-1,-2]
        dy = [-1,-2,-2,-1,1,2,2,1]
        
        @lru_cache(None)
        def dfs(i, j, K):
            #if out of boundary with k, bruh no way 
            if i < 0 or j < 0 or i >= n or j >= n:
                return 0
            if K == 0:      #inside board
                return 1
            p = 0
            for y in range(8):
                p += (1/8)*dfs(i+dx[y], j+dy[y], K-1)
            return p
        
        return dfs(row, column, K)
    #8 side gaye the har jagah 1 mila to ans 1/8x8=1, hua and kahi kahi 1 milka to kuch decimel me
        
#         #2
#         cur = [[0 for _ in range(n)] for _ in range(n)] #for state k=0
#         cur[row][column] = 1.0
        
#         for i in range(1, K):
#             pre = cur
#             cur = [[0 for _ in range(n)] for _ in range(n)] #for  every new state k
            
#             for j in range(n):
#                 for k in range(n):
                    
#                     for y in range(8):
#                         xx = j + dx[y]
#                         yy = k + dy[y]
#                         if xx>=0 and yy>=0 and xx<n and yy<n:
#                             cur[j][k] += (1/8)*pre[xx][yy]
        
#         ans = 0
#         for i in range(n):
#             for j in range(n):
#                 ans += cur[i][j]
#         return ans