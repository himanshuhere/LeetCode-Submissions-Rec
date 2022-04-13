class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        rows, cols = len(matrix), len(matrix[0])
        l, r = 0, cols - 1
        t, b = 0, rows - 1
        d = 0   #direction
        
        while l <= r and t <= b:
            if d == 0:
                for i in range(l, r+1):
                    ans.append(matrix[t][i])
                t += 1
                d = 1
                
            elif d == 1:
                for i in range(t, b+1):
                    ans.append(matrix[i][r])
                r -= 1
                d = 2
                
            elif d == 2:
                for i in range(r, l-1, -1):
                    ans.append(matrix[b][i])
                b -= 1
                d = 3
                
            else:
                for i in range(b, t-1, -1):
                    ans.append(matrix[i][l])
                l += 1
                d = 0
        
        return ans
                