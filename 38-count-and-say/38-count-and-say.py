class Solution:
    def countAndSay(self, n: int) -> str:
        def next_num(s):
            i = 0
            res = ""
            while i < len(s):
                c = 1
                ch = s[i]
                while i < len(s)-1 and s[i] == s[i+1]:
                    c += 1
                    i +=1
                res += (str(c) + ch)
                i += 1
            return res
        
        s = "1"
        for _ in range(1, n):
            s = next_num(s)
        return s