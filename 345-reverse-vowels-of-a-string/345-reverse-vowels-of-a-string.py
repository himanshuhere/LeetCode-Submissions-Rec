class Solution:
    def reverseVowels(self, str: str) -> str:
        l, r = 0, len(str)-1
        s = list(str)
        vow = "aeiouAEIOU"
        
        while l < r:
            if s[l] in vow and s[r] in vow:
                s[l], s[r] = s[r], s[l]
                l +=1
                r -=1
            if s[l] not in vow:
                l += 1
            if s[r] not in vow:
                r -= 1
        return "".join(s)