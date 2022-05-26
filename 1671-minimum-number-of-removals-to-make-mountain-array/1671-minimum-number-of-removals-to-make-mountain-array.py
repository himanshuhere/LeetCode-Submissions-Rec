class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        #Find the LBS, longest bitonic subsequence and then subtract it from the total lenght. you ll get your maountain fucker
        
        #LBS from LIS see
        n = len(nums)
        inc = [0] * n
        dec = [0] * n
        
        #lis
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    inc[i] = max(inc[i], inc[j] + 1)
          
        #lds
        for i in range(n-1,-1,-1):
            for j in range(n-1,i,-1):
                if nums[i] > nums[j]:
                    dec[i] = max(dec[i], dec[j] + 1)
        
        res = 0
        for i in range(0,n):
            if inc[i] > 0 and dec[i] > 0:
                res = max(res, inc[i] + dec[i])
                
        return n - res - 1