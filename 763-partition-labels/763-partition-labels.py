class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastocc = [0]*26
        for i, ch in enumerate(s):
            lastocc[ord(ch)-ord('a')] = i
            
        ans = []
        n = len(s)
        i = 0
        while i < n:
            last = lastocc[ord(s[i])-ord('a')] 
            j = i
            while j < n and j <= last:
                if lastocc[ord(s[j])-ord('a')] > last:
                    last = lastocc[ord(s[j])-ord('a')]
                j += 1            
            pre = sum(ans)
            ans.append((last-pre)+1)
            i = j
        return ans