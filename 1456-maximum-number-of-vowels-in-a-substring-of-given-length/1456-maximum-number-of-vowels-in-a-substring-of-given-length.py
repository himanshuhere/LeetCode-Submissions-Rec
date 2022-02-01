class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        #fixed sliding window
        i, j =0, 0
        ans = 0
        vowels = 0
        while j < len(s):
            if s[j] in ['a','e','i','o','u']:
                vowels+=1
            if j-i+1==k:
                ans = max(ans, vowels)
                if s[i] in ['a','e','i','o','u']:
                    vowels -= 1
                i+=1
            j+=1
        return ans
        