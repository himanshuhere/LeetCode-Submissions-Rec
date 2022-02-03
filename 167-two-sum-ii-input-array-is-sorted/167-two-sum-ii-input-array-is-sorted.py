class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        lo, hi = 0, len(nums)-1
        while lo < hi:
            if nums[lo] + nums[hi] < target:
                lo += 1
            elif nums[lo] + nums[hi] > target:
                hi -= 1
            else:
                return [lo+1, hi+1]
        