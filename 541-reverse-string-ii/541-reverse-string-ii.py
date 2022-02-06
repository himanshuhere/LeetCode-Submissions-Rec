class Solution:
    def reverseStr(self, s: str, k: int) -> str:
            s = list(s)
            for i in range(0, len(s), 2*k):
                s[i:i+k] = reversed(s[i:i+k])
            return "".join(s)
        
        
            
            if k > len(s):
                return s[::-1]
            
            n = len(s)
            i = 0
            s = list(s)
            while i < len(s) :
                p1, p2 = i, i + k-1
                P2 = min(i+k-1, n-1)
                    
                while p1 < p2:
                    s[p1], s[p2] = s[p2], s[p1]
                    p1 += 1
                    p2 -= 1
                    
                i += 2*k
                
            return ''.join(s)
