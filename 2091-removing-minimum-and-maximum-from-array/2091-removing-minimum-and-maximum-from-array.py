class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        i = nums.index(min(nums))
        j = nums.index(max(nums))
        n = len(nums)
        
        return min( max(j+1, i+1), max(n-i, n-j), i+1+n-j, j+1+n-i)
    