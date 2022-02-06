class Solution:
    def reversePrefix(self, w: str, ch: str) -> str:
        w = list(w)
        j = 0
        while j < len(w):
            if w[j] == ch:
                break
            j += 1
        if j == len(w): return "".join(w)
        
        i = 0
        while i < j:
            w[i], w[j] = w[j], w[i]
            i += 1
            j -= 1
        return "".join(w)
        