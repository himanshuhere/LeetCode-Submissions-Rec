class Solution:
    def minDistance(self, text1: str, text2: str) -> int:
        #we ll try to use LCS here and solve okay lets see
        m = len(text1)
        n = len(text2)
        t = [[0 for _ in range(n+1)] for _ in range(m+1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                
                if text1[i-1] == text2[j-1]:
                    t[i][j] = t[i-1][j-1] + 1
                    
                else:
                    t[i][j] = max(t[i][j - 1], t[i - 1][j])


        lcs_ans = t[m][n]
        
        return (m - lcs_ans) + (n - lcs_ans)
        
#         total_del_text1 = m - lcs_ans
#         total_del_text2 = n - lcs_ans
        
#         return total_del_text1 + total_del_text2