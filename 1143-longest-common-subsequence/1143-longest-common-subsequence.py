class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
#         @lru_cache(None)
#         def fn(i, j):
#             if i == 0 or j == 0:
#                 return 0
#             if text1[i-1] == text2[j-1]:
#                 print(text1[i-1])
#                 return 1 + fn(i-1, j-1)
#             else:
#                 return max(fn(i-1, j), fn(i, j-1))
            
#         m = len(text1)
#         n = len(text2)
#         return fn(m, n)
        
#         m = len(text1)
#         n = len(text2)
#         t = [[0 ]*(n+1) for _ in range(m+1)]

#         for i in range(1, m + 1):
#             for j in range(1, n + 1):
                
#                 if text1[i-1] == text2[j-1]:
#                     t[i][j] = t[i-1][j-1] + 1
                    
#                 else:
#                     t[i][j] = max(t[i][j - 1], t[i - 1][j])


#         return t[m][n]
    
        m = len(text1)
        n = len(text2)
        prev = [0]*(n+1)        #column lenght

        for i in range(1, m + 1):
            cur = [0]*(n+1)
            for j in range(1, n + 1):
                if text1[i-1] == text2[j-1]:
                    cur[j] = prev[j-1] + 1
                else:
                    cur[j] = max(cur[j - 1], prev[j])
            prev = cur
        return prev[n]
    