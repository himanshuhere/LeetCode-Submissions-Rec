class Solution:
    def validPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                #check for right i = i+1, or left j=j-2. any one true will fine
                return self.pal(s, i+1, j) or self.pal(s, i, j-1)
            
        return True     #it was already a palindrom
        

    
    def pal(self, s, i, j):
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
        
        return True