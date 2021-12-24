class Solution:
    def maxDistance(self, A: List[int]) -> int:
        i, j = 0, len(A)-1
        if A[i] != A[j]:
            return j-i
        
        ans = 0
        last = A[-1]
        while last == A[i]:
            i += 1
        ans = max(ans, j-i)
        
        i = 0
        first = A[0]
        while first == A[j]:
            j -= 1
        ans = max(ans, j-i)

            
        return ans
