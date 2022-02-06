class Solution:
    def reverseWords(self, s: str) -> str:
        #return ' '.join(s.split()[::-1])
    
        i = 0
        while i < len(s) and s[i] == " ":
            i += 1
        j = len(s)-1
        while j >= 0 and s[j] == " ":
            j -= 1
        
        j += 1
        
        ans = ""
        while i < j:
            if s[i] == " ":
                i+=1
                continue
                
            cur = ""
            while i < j and s[i] != " ":
                cur += s[i]
                i += 1
            ans = " " + cur + ans
            
        return ans[1:]