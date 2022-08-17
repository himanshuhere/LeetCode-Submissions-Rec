class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @lru_cache(None)
        def f(i, cur):
            if i==n:
                if cur in dic:
                    return True
                return False
            
            cur += s[i]
            
            if cur in dic:
                return f(i+1, cur) or f(i+1, "")
            else:
                return f(i+1, cur)
    
        n = len(s)
        dic = set(wordDict)
        return f(0, "")
    
    #Brute time is 2^n, as max two choices but string concat then N*2^N
    #DP time : n*n*k, n and n for dp states and k for concat if needed