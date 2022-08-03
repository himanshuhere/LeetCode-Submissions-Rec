class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @lru_cache(None)
        def f(i):
            if i == 0 or i == 1:
                return cost[i]
            return cost[i]+min(f(i-1), f(i-2))
        return min(f(len(cost)-2), f(len(cost)-1))