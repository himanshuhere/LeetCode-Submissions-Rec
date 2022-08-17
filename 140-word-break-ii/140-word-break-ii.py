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
    #word break 1, 2 both can be done with dp and hashset, and more optimization is trie.
    #So first always give DP, then agar aur to usi code me optimize kardo
    #take care with final etc in word break 2
    
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        @lru_cache(None)
        def f(i, node, final, cur):
            if i==n:
                if node.end:
                    res.append(final+cur)
                    return
                return
            if s[i] not in node.ch:
                return
            
            cur += s[i]
            
            node = node.ch[s[i]]
            
            #print(final, cur)
            if node.end:
                return f(i+1, root, final+cur+" ", "") or f(i+1, node, final, cur)
            else:
                return f(i+1, node, final, cur)
    
        n = len(s)
        res = []
        root = TN()
        for w in wordDict:
            root.insert(w)
        f(0, root, "", "")
        return res
    
    
#     def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
#         @lru_cache(None)
#         def f(i, final, cur):
#             if i==n:
#                 if cur in dic:
#                     res.append(final+cur)
#                     return
#                 return
            
#             cur += s[i]
#             #print(final, cur)
#             if cur in dic:
#                 return f(i+1, final+cur+" ", "") or f(i+1, final, cur)
#             else:
#                 return f(i+1, final, cur)
    
#         n = len(s)
#         res = []
#         dic = set(wordDict)
#         f(0, "", "")
#         return res
    
#     #Brute time is 2^n, as max two choices but string concat then N*2^N
#     #DP time : n*n*k, n and n for dp states and k for concat if needed