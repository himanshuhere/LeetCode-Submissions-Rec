class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)
        left, right = [n]*n, [n]*n
        #left[0] = 0
        for i in range(n):
            if seats[i] == 1:
                left[i] = 0
            elif i > 0:
                left[i] = left[i-1] + 1 
        #right[-1] = 0
        for i in range(n-1, -1, -1):
            if seats[i] == 1:
                right[i] = 0
            elif i < n-1:
                right[i] = right[i+1] + 1 
        
        ans = 0
        for i in range(n):
            if seats[i] == 0:
                ans = max(ans, min(left[i], right[i]))
        return ans
            
        