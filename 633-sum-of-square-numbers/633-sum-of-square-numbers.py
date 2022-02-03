class Solution:
    def judgeSquareSum(self, c: int) -> bool:
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
                