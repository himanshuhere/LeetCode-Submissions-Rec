class Solution:
    def addDigits(self, num: int) -> int:
        ans = 0
        while True:
            while num:
                ans += num%10
                num //= 10
            if ans < 10:    return ans
            num = ans
            ans = 0
            