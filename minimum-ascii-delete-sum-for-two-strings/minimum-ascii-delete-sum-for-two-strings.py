class Solution:
    def minimumDeleteSum(self, text1: str, text2: str) -> int:
        
        #we ll try to use LCS here and solve okay lets see
        m = len(text1)
        n = len(text2)
        t = [[0 for _ in range(n+1)] for _ in range(m+1)]
        
        lcs = ""        #might not be acc but we need char participating there
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                
                if text1[i-1] == text2[j-1]:
                    t[i][j] = ord(text1[i-1]) + t[i-1][j-1]     #instead of 1
                else:
                    t[i][j] = max(t[i][j - 1], t[i - 1][j])
                    
        lcs_ans = t[m][n]
        
        n1 = sum(ord(c) for c in text1)
        n2 = sum(ord(c) for c in text2)
        
        return n1 + n2 - 2 * lcs_ans