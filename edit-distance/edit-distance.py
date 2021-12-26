class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @lru_cache(None)
        def dp(i, j):
            if i == 0: return j  # Need to insert j chars
            if j == 0: return i  # Need to delete i chars
            
            if word1[i-1] == word2[j-1]:      #No penalty
                return dp(i-1, j-1)
            else:
                ins = dp(i, j-1)
                dlt = dp(i-1, j)
                rep = dp(i-1, j-1)
            return 1 + min(ins, dlt, rep)
        
        return dp(len(word1), len(word2))
