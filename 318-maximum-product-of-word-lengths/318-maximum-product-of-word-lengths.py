class Solution:
    def maxProduct(self, w: List[str]) -> int:
        def f(s1, s2):
            for i in s1:
                if i in s2:
                    return False
            return True
        
        ans = 0
        for i in range(len(w)):
            for j in range(i+1, len(w)):
                if f(w[i], w[j]):
                    ans = max(ans, len(w[i])*len(w[j]))
        return ans