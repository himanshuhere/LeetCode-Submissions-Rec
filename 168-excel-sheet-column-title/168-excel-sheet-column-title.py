class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ""
        n = columnNumber
        while n:
            n-=1            #offset as here A-1 not A-0, yes observation nothing logical
            c = chr(n%26 + ord('A'))     
            res += c
            n = n//26
        return res[::-1]