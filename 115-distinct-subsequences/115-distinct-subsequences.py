class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        #See carefully, it is count ways so base case 0/1 and all state calls
        #two string, keep an index on both
        m, n = len(s), len(t)
        
#         @lru_cache(None)
#         def f(i, j):
#             if j >= n:      #pehle i ke liye likh rha tha ans hi nhi ayega, apan ko bas ye dekhna hai j exhauset hua hai mtlb we have matched all t, kuki apan j+1 matching wakt hi kar rhe else wahi khada rahega
#                 return 1
#             if i >= m:
#                 return 0
            
#             if s[i] == t[j]:
#                 return f(i+1, j) + f(i+1, j+1)
#             else:
#                 return f(i+1, j)
        
#         return f(0, 0)
#     #recurions - exponential/O(m+n) aux space
#     #memoized  - O(m*n)/O(m*n) + O(m+n)
#     #tab - o(m*n)/O(m*n)
        
#         #See kahani
#         #1
#         def f(i, j):
#             if j >= n:    return 1
#             if i >= m:    return 0
#             if s[i] == t[j]:
#                 return f(i-1, j) + f(i-1, j-1)
#             else:
#                 return f(i-1, j)
#         return(m-1, n-1)
        
        #2
        # dp = [[0]*(n+1) for _ in range(m+1)]
        # for i in range(m+1):
        #     dp[i][0] = 1
        # for i in range(1, m+1):
        #     for j in range(1, n+1):
        #         if s[i-1] == t[j-1]:
        #             dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
        #         else:
        #             dp[i][j] = dp[i-1][j]
        # return dp[-1][-1]

        #3
        prev = [0]*(n+1)
        prev[0] = 1
        cur = [0]*(n+1)
        cur[0] = 1
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s[i-1] == t[j-1]:
                    cur[j] = prev[j] + prev[j-1]
                else:
                    cur[j] = prev[j]
            prev = copy.copy(cur)       #ye direct ref attach karo but j loop k pehle cur har bar fill karna pdega same hi hai almost
        return prev[-1]
        
        #more optimization
