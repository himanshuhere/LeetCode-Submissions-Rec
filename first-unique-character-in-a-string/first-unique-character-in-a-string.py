class Solution:
    def firstUniqChar(self, s: str) -> int:
        c=Counter(s)
        for ind,i in enumerate(s):
            if c[i] == 1:
                return ind
        return -1