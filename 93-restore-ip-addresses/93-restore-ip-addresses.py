class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        def valid(lst):
            for s1 in lst:
                if s1[0]=="0" and len(s1)>1:         #more zeroes
                    return False
                if not (0<=int(s1)<=255):
                    return False
            return True
        
        def dfs(i, cur, par):
            if i == n or par == 4:          #if any then get inside
                if i == n and par == 4:     #if both then only right
                    res.append(cur[:-1])    #remove last .
                return
                
                    
            dfs(i+1, cur+s[i]+".", par+1)
            
            if i+1 < n and valid([s[i:i+2]]):
                dfs(i+2, cur+s[i:i+2]+".", par+1)
                
            if i+2 < n and valid([s[i:i+3]]):
                dfs(i+3, cur+s[i:i+3]+".", par+1)
        
        res = []
        n = len(s)
        dfs(0, "", 0)
        return res
            
                        
        
        
#         for i in range(1, 4):           #1,2,3
#             for j in range(i+1, i+4):
#                 for k in range(j+1, j+4):
#                     if k >= len(s):
#                         break
#                     s1 = s[:i]
#                     s2 = s[i:j]
#                     s3 = s[j:k]
#                     s4 = s[k:]
                    
#                     if valid([s1,s2,s3,s4]):
#                         ans.append(s1+"."+s2+"."+s3+"."+s4)
#         return ans
    
    #substring - o(n)
    #three loops constant so, 3^3, each loop possibility is 3 too
    #n * 3 ^ 3 = o(n)