class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #sorted thus no map, just two pointer
        
        lo, hi = 0, len(nums)-1
        while lo < hi:
            if nums[lo] + nums[hi] < target:
                lo += 1
            elif nums[lo] + nums[hi] > target:
                hi -= 1
            else:
                return [lo+1, hi+1]         #take care as ans wants 1-based indexing