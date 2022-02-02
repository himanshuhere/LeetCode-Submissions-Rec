class Solution:
    def maxArea(self, height: List[int]) -> int:
        #Two edge pointer + Greedy movement of pointers
        l, r = 0, len(height) - 1
        area = 0
        
        #l<=r, wil work too, thing practical, woudl one piller make sence? plus 2 <= n <= 105
        
        while l < r:         
            if height[l] < height[r]:
                area = max(area, (r-l)*height[l])   #r-l = width, smaller height
                l += 1                              #r is bigger, move l might get bigger area next (greed)
            else:
                area = max(area, (r-l)*height[r])
                r -= 1
        return area