class Solution:
    def convert(self, s: str, n: int) -> str:
        if n == 1:
            return s
        
        res = ""
        jump = 2 * (n - 1)
        
        for i in range(n):
            for j in range(i, len(s), jump):
                res += s[j]         #first col of each row
                #middle rows handles diagonal ele/ignore first n last row
                diagonal_jump = jump - 2 * i
                if i > 0 and i < n - 1 and j + diagonal_jump < len(s):
                    res += s[j + diagonal_jump]
        return res
                