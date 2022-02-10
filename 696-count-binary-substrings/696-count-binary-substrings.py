class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        #o(n^2)
        ans = 0
        for i in range(len(s)):
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] =='0' and s[r] == '1':
                l-=1
                r+=1
                ans+=1
            
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] =='1' and s[r] == '0':
                l-=1
                r+=1
                ans+=1
                
        return ans
                
        
        #whiles origin pe hi chalege like 01 ya 10, else k liye nhi 