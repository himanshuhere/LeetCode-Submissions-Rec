class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) > len(set(nums))
            #n^2 = two loop
        #nlogn = sort
        #n/n map or set
        