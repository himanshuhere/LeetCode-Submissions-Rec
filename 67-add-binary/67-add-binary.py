class Solution:
    def addBinary(self, a: str, b: str) -> str:
        #return bin(int(a,2)+int(b,2))[2::]
        
        m, n = len(a)-1, len(b)-1
        carry = 0
        res = ""
        curr = 0
        
        while m >= 0 or n >= 0:
            p = int(a[m]) if m >= 0 else 0
            q = int(b[n]) if n >= 0 else 0
            
            curr = p + q + carry
            res = str(curr%2) + res     #imp to noticce
            carry = curr // 2
            
            m -= 1
            n -= 1
            
        return res if carry == 0 else "1" + res