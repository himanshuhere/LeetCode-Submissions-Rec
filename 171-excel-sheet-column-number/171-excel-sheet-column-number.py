class Solution:
    def titleToNumber(self, col: str) -> int:
        res = 0
        for ch in col:
            res = res*26 + (ord(ch) - ord('A') + 1)
        return res