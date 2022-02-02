class Solution:
    def maxSatisfied(self, cust: List[int], grum: List[int], k: int) -> int:
        
        i, j = 0, 0
        ans = 0
        sm = 0
        tot = sum([cust[x] if grum[x]==0 else 0 for x in range(len(cust))])
        
        while j < len(cust):
            if grum[j]==1:
                sm += cust[j]
            #bcs 0 count is already in tot
            if j-i+1 == k:
                ans = max(ans, tot+sm)
                if grum[i] == 1:
                    sm -= cust[i]
                i += 1
            j += 1
        
        return ans