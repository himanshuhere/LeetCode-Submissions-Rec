class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        k = k%(m*n)
        line = []
        for i in range(m):
            for j in range(n):
                line.append(grid[i][j])
              
        #1 2 3 4 5 6 7 8 9 = 9 1 2 3 4 5 6 7 8
        line = line[-k:] + line[:len(line)-k]
        for i in range(len(line)):
            grid[(i//n)%m][i%n] = line[i]
        return grid
        
        
#         m, n = len(grid), len(grid[0])
#         k = k%(m*n)
        
#         ans = [[0]*n for _ in range(m)]
#         for i in range(m):
#             for j in range(n):
#                 newrow = i + k//n
#                 newcol = j + k%n
#                 ans[newrow%m][newcol%n] = grid[i][j]
#         return ans