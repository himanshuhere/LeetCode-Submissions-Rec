class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        #two pointer o(m+n) or o max(m,n) == j for bigger string i for smaller, run j loop if i == j then incriment i else or not else incriment j always, at last u have matching char lenght in i match it with string size
        
        if len(s) == 0:
            return True
        if len(t) == 0:
            return False 
        
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1    
        return i == len(s)
    
    #intuitive is lcs
    #lcs of two string cud be 0 to min(s1,s2), this case we ll find lcs and match its size with s1 if yes then return true
        m = len(s)
        n = len(t)
        tt = [[0]*(n+1) for _ in range(m+1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i-1] == t[j-1]:
                    tt[i][j] = tt[i-1][j-1] + 1   
                else:
                    tt[i][j] = max(tt[i][j - 1], tt[i - 1][j])
                    
        lcs_ans = tt[m][n]
        return lcs_ans == len(s)