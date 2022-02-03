class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #two sum with one extra loop wud have amny issue has there have uniqueness and here duplicates
        #this is the best
        nums.sort()        
        n = len(nums)
        res = []    
        target = 0
        
        for i in range(0, n-2):
			# avoid repetition
            if i == 0 or (i > 0 and nums[i] != nums[i-1]):
                target = -nums[i]
                lo, hi = i+1, n-1
                
                while lo < hi:
                    if nums[lo] + nums[hi] > target:
                        hi -=1
                    elif nums[lo] + nums[hi] < target:
                        lo += 1
                    else:
                        res.append([nums[i], nums[lo], nums[hi]])
                        lo += 1
                        hi -= 1
                        # avoid repetition
                        while lo < hi and nums[lo] == nums[lo-1]:   lo += 1
                        while lo < hi and nums[hi] == nums[hi+1]:   hi -= 1


        return res