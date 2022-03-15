class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        #o(n) string algo in notes, lets do DP here
        
        @lru_cache(None)
        def f(i, j):
            if i < 0 and j < 0:
                return True
            if j < 0 and i >= 0:    #if pattern ends, no chance
                return False
            
            if i < 0 and j >= 0:    #only if all asterick *, else not possible like , "", "*****"
                for k in range(0, j+1):
                    if p[k] != '*':
                        return False
                return True
                
            
            if s[i] == p[j] or p[j] == '?':
                return f(i-1, j-1)
            
            elif p[j] == '*':
                return f(i, j-1) or f(i-1, j)
            else:
                return False            #straight not matching and no ?, *
            
        return f(len(s)-1, len(p)-1)
                