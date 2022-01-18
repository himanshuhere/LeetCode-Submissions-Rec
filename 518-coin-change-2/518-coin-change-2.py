class Solution:
    def change(self, amt: int, coins: List[int]) -> int:
        #Unbounded knapsack
        @lru_cache(None)
        def f(i, amt):
            if amt == 0:
                return 1
            if i == -1:
                return 0
            if coins[i] <= amt:
                return f(i, amt-coins[i]) + f(i-1,amt)
            else:
                return f(i-1, amt)
        
        return f(len(coins)-1, amt)