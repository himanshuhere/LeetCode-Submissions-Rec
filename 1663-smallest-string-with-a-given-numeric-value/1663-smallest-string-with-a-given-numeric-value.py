class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        #Think greedily.
        #If you build the string from the end to the beginning, it will always be optimal to put the highest possible character at the current index.


        ans = ""
        while n:
            if k-(n-1) >= 26:
                ans += 'z'
                k -= 26
            else:
                ans += chr(97 + k-(n-1) - 1)
                k -= (k-(n-1))
            n -= 1
        return ans[::-1]
            