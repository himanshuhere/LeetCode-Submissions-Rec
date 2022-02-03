class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        #two pointer, c will give TLE. since numbers are sorted kinda two pointer works.
        #make sure to use int(sqrt), else was giving wrong answer
        #0 is valid so keep at lo like 0, 10 = 100
        
        lo, hi = 0, int(sqrt(c))
        while lo <= hi:
            cur = lo*lo + hi*hi
            if cur < c:
                lo += 1
            elif cur > c:
                hi -= 1
            else:
                return True
        return False
            
        #Time complexity is O(sqrt(c)), space complexity is O(1).

