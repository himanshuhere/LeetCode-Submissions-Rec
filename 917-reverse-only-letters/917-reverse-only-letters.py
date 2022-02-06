class Solution:
    def reverseOnlyLetters(self, st: str) -> str:
        s = list(st)
        i, j = 0, len(s)-1
        while i < j:
            if not ((65 <= ord(s[i]) <= 90) or (97 <= ord(s[i]) <= 122)):
                i += 1
            elif not ((65 <= ord(s[j]) <= 90) or (97 <= ord(s[j]) <= 122)):
                j -= 1
            else:
                s[i], s[j] = s[j], s[i]
                j-=1
                i+=1
        return "".join(s)