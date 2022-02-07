class Solution:
    def reverseWords(self, s: str) -> str:
        s = list(s)
        
        def rev(cur):
            i, j = 0, len(cur)-1
            while i < j:
                cur[i], cur[j] = cur[j], cur[i]
                i += 1
                j -= 1
            return "".join(cur)
        
        cur = ""
        ans = ""
        for i in range(len(s)):
            if s[i] == " ":
                cur = rev(list(cur))
                ans += cur + " "
                cur = ""
            else:
                cur += s[i]

        #last word
        cur = rev(list(cur))
        ans += cur
        return ans
        
        
        #ls = s.split(' ')
        # for i in range(len(ls)):
        #     ls[i] = ls[i][::-1]
        # return ' '.join(ls)
                
            