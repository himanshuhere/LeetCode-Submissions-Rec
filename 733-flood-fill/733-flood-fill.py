class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        def dfs(i, j):
            if i<0 or j<0 or i>=m or j>=n or image[i][j]==newColor or image[i][j]!=oldcolor:
                return 
            image[i][j] = newColor
            dfs(i+1,j)
            dfs(i, j+1)
            dfs(i-1,j)
            dfs(i,j-1)
        
        m, n = len(image), len(image[0])
        oldcolor = image[sr][sc]
        dfs(sr,sc)
        return image
    
    #image[i][j]==newColor or image[i][j]!=oldcolor: both condition are necesarry yes
