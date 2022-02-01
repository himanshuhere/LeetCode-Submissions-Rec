class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        i, j = 0, 0
        m = defaultdict(int)
        ans = 0
        c=0
        while j < len(s):
            m[s[j]] += 1
            if m[s[j]] == 1:
                c+=1
                
            while c==3:
                ans += len(s) - j       #imp to notice
                if s[i] in m:
                    m[s[i]] -= 1
                    if m[s[i]]==0:
                        c-=1
                i+=1
            j+=1
        return ans