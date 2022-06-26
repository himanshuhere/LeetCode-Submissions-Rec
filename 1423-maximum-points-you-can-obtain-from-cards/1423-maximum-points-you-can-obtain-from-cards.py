class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        tot = sum(cardPoints)
        k = n-k
        if k == 0:
            return tot
        
        i, j, s = 0, 0, 0
        ans = math.inf
        while j < n:
            s += cardPoints[j]
            if j-i+1 == k:
                ans = min(ans, s)
                s -= cardPoints[i]
                i += 1
            j += 1
        return tot-ans
                
            