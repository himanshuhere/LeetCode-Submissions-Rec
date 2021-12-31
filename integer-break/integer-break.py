class Solution:
    def integerBreak(self, n: int) -> int:
        @lru_cache(None)
        def dp(n, k):
            if n == 0:
                if k == 2:
                    return 1
                return 0

            ans = 0
            for x in range(1, n + 1):
                ans = max(ans, dp(n - x, min(k + 1, 2)) * x)
            return ans

        return dp(n, 0)