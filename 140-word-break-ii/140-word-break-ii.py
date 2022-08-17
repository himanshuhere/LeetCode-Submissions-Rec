class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        @lru_cache(None)
        def f(i, final, cur):
            if i==n:
                if cur in dic:
                    res.append(final+cur)
                    return
                return
            
            cur += s[i]
            #print(final, cur)
            if cur in dic:
                return f(i+1, final+cur+" ", "") or f(i+1, final, cur)
            else:
                return f(i+1, final, cur)
    
        n = len(s)
        res = []
        dic = set(wordDict)
        f(0, "", "")
        return res
    
    #Brute time is 2^n, as max two choices but string concat then N*2^N
    #DP time : n*n*k, n and n for dp states and k for concat if needed