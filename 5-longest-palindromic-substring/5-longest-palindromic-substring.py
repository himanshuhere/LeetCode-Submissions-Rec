class Solution:
    def longestPalindrome(self, s: str) -> str:
        # starting at l,r expand outwards to find the biggest palindrome
        def palindromeAt(s, l, r):    
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]
        
        res = ""
        for i in range(len(s)):        
            odd  = palindromeAt(s, i, i)
            even = palindromeAt(s, i, i+1)

            res = max(res, odd, even, key=len)
        return res

    
    #why not LPS.bcs LPSubstring matrix wd have 0 in matrix and thus you cant deciee where to move when matching is done.
    
    
    
    
        #dp - LPS - LCSubtring one
        if s is "":
            return ""
        
        rev = s[::-1]
        dp = [[0 for i in range(len(s))] for j in range(len(s))]
        
        max_len = 0
        max_end = 0
        
        for i in range(len(s)):
            for j in range(len(s)):
                
                if s[i] == rev[j]:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i-1][j-1] + 1
                        
                if dp[i][j] > max_len:
                    if i-dp[i][j]+1 == len(s)-1-j:
                        max_len = dp[i][j]
                        max_end = i
                
        return s[max_end - max_len + 1: max_end + 1]
    
    
    
        #dp - diagonal one
        #P(i, j)=(P(i+1, j-1) and s[i] == s[j])
        if s is "":
            return s
        res = ""
        dp = [[None for i in range(len(s))] for j in range(len(s))]
        
        for j in range(len(s)):
            for i in range(j):
                if i == j:      #target one char diagonally
                    dp[j][i] = True
                elif j == i+1:  #target two adj char one line above diag
                    dp[j][i] = (s[i] == s[j])
                else:           #rest of matrix
                    dp[j][i] = (dp[j-1][i+1] and s[i] == s[j])
                    
                if dp[j][i] and j - i + 1 > len(res):   #since we want the str not len. thus this operation
                    res = s[i:j+1]
        return res
        
