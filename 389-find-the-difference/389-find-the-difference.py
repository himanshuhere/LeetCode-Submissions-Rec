class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ss = t
        s, t = Counter(s), Counter(t)
        for i in ss:
            if s[i] != t[i]:
                return i
        
        
        