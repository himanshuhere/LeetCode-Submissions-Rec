class TN:
    def __init__(self):
        self.ch = {}
        self.end = False
    
    def insert(self, word):
        node = self
        for c in word:
            if c not in node.ch:
                node.ch[c] = TN()
            node = node.ch[c]
        node.end = True
        
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        @lru_cache(None)
        def f(i, node, cur):
            if i==n:
                if node.end:
                    return True
                return False
            
            if s[i] not in node.ch:
                return
            
            cur += s[i]
            
            node = node.ch[s[i]]
            
            #print(final, cur)
            if node.end:
                return f(i+1, root, "") or f(i+1, node, cur)
            else:
                return f(i+1, node, cur)
    
        n = len(s)
        root = TN()
        for w in wordDict:
            root.insert(w)
        return f(0, root, "")
    
        
        #DP
#         @lru_cache(None)
#         def f(i, cur):
#             if i==n:
#                 if cur in dic:
#                     return True
#                 return False
            
#             cur += s[i]
            
#             if cur in dic:
#                 return f(i+1, cur) or f(i+1, "")
#             else:
#                 return f(i+1, cur)
    
#         n = len(s)
#         dic = set(wordDict)
#         #return f(0, "")
    
    
#     #Brute time is 2^n, as max two choices but string concat then N*2^N
#     #DP time : n*n*k, n and n for dp states and k for concat if needed