class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        #Best technique
        def isomorphic(s):
            m = {}
            code = ""
            for i, c in enumerate(s):
                if c not in m:
                    m[c] = i
                code += str(m[c])
            return code
        
        res = []
        patcode = isomorphic(pattern)
        for w in words:
            if patcode == isomorphic(w):
                res += [w]
        return res
            