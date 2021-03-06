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
        
        for i in range(1, 4):           #1,2,3
            for j in range(i+1, i+4):
                for k in range(j+1, j+4):
                    if k >= len(s):
                        break
                    s1 = s[:i]
                    s2 = s[i:j]
                    s3 = s[j:k]
                    s4 = s[k:]
                    
                    if valid([s1,s2,s3,s4]):
                        ans.append(s1+"."+s2+"."+s3+"."+s4)
        return ans