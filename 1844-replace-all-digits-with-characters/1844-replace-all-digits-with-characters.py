class Solution:
    def replaceDigits(self, s: str) -> str:
        l = list(s)
        for i in range(1, len(l), 2):
            if i & 1:
                l[i] = chr(ord(l[i-1]) + int(l[i]))
        return "".join(l)