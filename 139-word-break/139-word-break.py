class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @lru_cache(None)
        def f(i, cur):
            if i==n:
                if cur in dic:
                    return True
                return False
            if cur in dic:
                return f(i+1, cur+s[i]) or f(i+1, s[i])
            else:
                return f(i+1, cur+s[i])
    
        n = len(s)
        dic = set(wordDict)
        return f(0, "")