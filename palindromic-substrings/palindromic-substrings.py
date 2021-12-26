class Solution:
    def countSubstrings(self, s: str) -> int:
        #Same idea - for any PALINDROME SUBSTRING - woi expanding algo
        
        def grow(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                self.count += 1
                left -= 1
                right += 1
        
        self.count = 0
        for i in range(len(s)):
            grow(i, i)        #oddly expand, will count single char as palidrome
            grow(i, i+1)      #even
        return self.count