class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        #o(1) space bas a=a+nb hi kar sakta hai
        n = len(nums)
        for i in range(len(nums)):
            nums[i] = nums[i] + n*(nums[nums[i]] % n)
        for i in range(len(nums)):
            nums[i] = nums[i]//n
        return nums