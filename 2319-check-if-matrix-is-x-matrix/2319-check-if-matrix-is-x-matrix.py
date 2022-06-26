class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        cl = len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i==j or i+j==cl-1:
                    if grid[i][j] == 0:
                        return False
                else:
                    if grid[i][j] != 0:
                        return False
        return True