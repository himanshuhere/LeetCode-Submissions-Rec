class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        k = n-k
        if k == 0:
            return sum(cardPoints)
        
        i = 0
        j = 0
        s = 0
        ans = math.inf
        while j < n:
            s += cardPoints[j]
            if j-i+1 == k:
                ans = min(ans, s)
                s -= cardPoints[i]
                i += 1
            j += 1
        return sum(cardPoints)-ans
                
            