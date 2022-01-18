class Solution:
    def coinChange(self, coins: List[int], amt: int) -> int:
        #Unbounded knapsack
#         @lru_cache(None)
#         def f(i, amt):
#             if amt == 0:
#                 return 0
#             if i == -1:
#                 return math.inf
            
#             if coins[i] <= amt: 
#                 return min(1 + f(i, amt-coins[i]), f(i-1,amt))
#             else:               
#                 return f(i-1, amt)
            
#         ans = f(len(coins)-1, amt)
#         return ans if ans < math.inf else -1
        
        n = len(coins)
        t = [[0 for _ in range(amt+1)] for _ in range(n+1)]
        for i in range(n+1):
            for j in range(amt+1):
                if i == 0:  t[i][j] = math.inf
                elif j == 0:    t[i][j] = 0
                elif coins[i-1] <= j:   
                    t[i][j] = min(1 + t[i][j-coins[i-1]], t[i-1][j])
                else:
                    t[i][j] = t[i-1][j]
                    
        return t[-1][-1] if t[-1][-1] < math.inf else -1
             
    
        