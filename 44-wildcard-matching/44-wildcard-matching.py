class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        #o(n) string algo in notes, lets do DP here
        
#         @lru_cache(None)
#         def f(i, j):
#             if i < 0 and j < 0:
#                 return True
#             if j < 0 and i >= 0:    #if pattern ends, no chance
#                 return False
            
#             if i < 0 and j >= 0:    #only if all asterick *, else not possible like , "", "*****"
#                 for k in range(0, j+1):
#                     if p[k] != '*':
#                         return False
#                 return True
                
            
#             if s[i] == p[j] or p[j] == '?':
#                 return f(i-1, j-1)
            
#             elif p[j] == '*':
#                 return f(i, j-1) or f(i-1, j)
#             else:
#                 return False            #straight not matching and no ?, *
            
#         return f(len(s)-1, len(p)-1)
    
    
    #SEE,
#     First, if MATCHING (ALSO INCLUDES ? CASE):
#         Simply shrink as matches

#     Second, if patter has *, so since * can ba matchew with 0 to n letters, thus we can match it with "" or in coding case we can skip * and we can match start with 1 or more so what looping no we are doing recursion anyway so better match with one char and move further putting start at same location. Every call have two branch in star case, first branch will leave star and ceond will leave other string char, both combines can help in skipp the n number of chars and go start matching with others.

#     Third, if no ? or *, and chars dont match just return False

# NOW, COMPLICATES BASE CASES, trying some cases you will get that both should exhausted together to return true, if any one of then exhausted before other return False, but wait wait wait there is one wildcard which helps in matching with empty string yes *, so better break two cases if patter is empty and string is remaining, no chance return False, but for vice versa we ONLY need *, ? cam match with char not empty thats why check for all *, if all * return True else return False
            
    
        #Now TABULATION, so lets first make it 1-based indexing carefully pls
#         @lru_cache(None)
#         def f(i, j):
#             if i == 0 and j == 0:
#                 return True
#             if j == 0 and i > 0:    #if pattern ends, no chance
#                 return False
            
#             if i == 0 and j > 0:    #only if all asterick *, else not possible like , "", "*****"
#                 for k in range(1, j+1):
#                     if p[k-1] != '*':
#                         return False
#                 return True
                
            
#             if s[i-1] == p[j-1] or p[j-1] == '?':
#                 return f(i-1, j-1)
            
#             elif p[j-1] == '*':
#                 return f(i, j-1) or f(i-1, j)
#             else:
#                 return False            #straight not matching and no ?, *
            
#         return f(len(s), len(p))
        
        #2D DP
#         m, n = len(s), len(p)
#         dp = [[False]*(n+1) for _ in range(m+1)]
#         dp[0][0] = True
        
#         for i in range(1, m+1):
#             dp[i][0] = False
        
#         for j in range(1, n+1):
#             flag = True
#             for k in range(1, j+1):    #if only till 0 to j, then use p[k]
#                 if p[k-1] != '*':
#                     flag = False
#                     break
#             dp[0][j] = flag
        
#         for i in range(1, m+1):
#             for j in range(1, n+1):
#                 if s[i-1] == p[j-1] or p[j-1] == '?':
#                     dp[i][j] = dp[i-1][j-1]
#                 elif p[j-1] == '*':
#                     dp[i][j] = dp[i][j-1] or dp[i-1][j]
#                 else:
#                     dp[i][j] = False   
#         return dp[-1][-1]
    
        #1D DP
        m, n = len(s), len(p)
        prev = [False]*(n+1)
        cur = [False]*(n+1)
        prev[0] = True
        
        for j in range(1, n+1):
            flag = True
            for k in range(1, j+1):    #if only till 0 to j, then use p[k]
                if p[k-1] != '*':
                    flag = False
                    break
            prev[j] = flag
        
        for i in range(1, m+1):
            cur[0] = False              #first col of evry row
            for j in range(1, n+1):
                if s[i-1] == p[j-1] or p[j-1] == '?':
                    cur[j] = prev[j-1]
                elif p[j-1] == '*':
                    cur[j] = cur[j-1] or prev[j]
                else:
                    cur[j] = False 
            prev = copy.copy(cur)
            
        return prev[-1]
        
    
        
        
        
                