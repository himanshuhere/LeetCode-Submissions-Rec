class Solution:
    def change(self, amt: int, coins: List[int]) -> int:
        #Unbounded knapsack
#         @lru_cache(None)
#         def f(i, amt):
#             if amt == 0:
#                 return 1
#             if i == -1:
#                 return 0
#             #if amt < 0:  return 0 and remove if else
#             if coins[i] <= amt:
#                 return f(i, amt-coins[i]) + f(i-1,amt)
#             else:
#                 return f(i-1, amt)
        
#         return f(len(coins)-1, amt)
        
        n = len(coins)
        t = [[0 for _ in range(amt+1)] for _ in range(n+1)]
        for i in range(n+1):
            for j in range(amt+1):
                if i == 0:  t[i][j] = 0
                elif j == 0:    t[i][j] = 1
                elif coins[i-1] <= j:   
                    t[i][j] = t[i][j-coins[i-1]] + t[i-1][j]
                else:
                    t[i][j] = t[i-1][j]
        return t[-1][-1]
             
    
        