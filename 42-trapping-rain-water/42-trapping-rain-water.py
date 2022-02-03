class Solution:
    def trap(self, height: List[int]) -> int:
    #pls see notes all solution., understand the intuition, extention of prefix/suffix
    #crux = min(lmax, rmax)-current_height
        #1 understading intuition here
        n = len(height)
        l, r = 0, n-1
        lmax, rmax = 0, 0
        res = 0
        while l < r:
            #updates maxes
            if height[l] > lmax:    lmax = height[l]
            if height[r] > rmax:    rmax = height[r]
        
            #compute water on curr pillar
            if lmax < rmax:
                res += lmax - height[l]
                l+=1
            else:
                res += rmax - height[r]
                r-=1
        return res
        
        
        #2 striver
        n = len(height)
        le, ri = 0, n - 1
        lmax = rmax = 0
        ans = 0
        
        while le < ri:
            
            if height[le] < height[ri]:    #making sure right is max that left, thus we can store water
                if height[le] >= lmax: lmax = height[le]    #it is 0 zero water then
                else: ans += lmax - height[le]
                le += 1
                
            else:
                if height[ri] >= rmax: rmax = height[ri]
                else: ans += rmax - height[ri]
                ri -= 1
        return ans
    
    #2 aditya's prefix and suffix. we can also use suffix only
        n = len(height)
        max_l = max_r = water_store = [-1] * n
        max_l[0] = height[0]
        max_r[n-1] = height[n-1]
        
        for i in range(1, n):
            max_l[i] = max(max_l[i-1], max_l[i])
            
        for i in range(n-2, -1, -1):
            max_r[i] = max(max_r[i+1], max_r[i])
        
        for i in range(n):
            water_store[i] = min(max_l[i], max_r[i]) - height[i]
        
        return sum(water_store)
        
        
                