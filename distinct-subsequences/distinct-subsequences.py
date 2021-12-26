class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        @lru_cache(None)
        def dfs(i, j):
            if j == len(t): #we got one ans
                return 1
            if i == len(s): #nothing we got nothing s hi paar ho gyi j k pehle
                return 0
 
            if s[i]==t[j]:
                return dfs(i+1, j+1) + dfs(i+1, j)  #j nhi kuki wo t hai skip nhi kar sakte try karna hai apan ko s me kud kaad ke 
            else:
                return dfs(i+1, j)  #dsnt mathced so jump
                
        
        return dfs(0,0)