class Solution:
    def wordPattern(self, p: str, s: str) -> bool:
        words, m = s.split(' '), dict()

        if len(p) != len(words): return False
        if len(set(p)) != len(set(words)): return False # for the case w = ['dog', 'cat'] and p = 'aa'

        for i in range(len(words)):
            if words[i] not in m: 
                m[words[i]] = p[i]
            elif m[words[i]] != p[i]: 
                return False

        return True