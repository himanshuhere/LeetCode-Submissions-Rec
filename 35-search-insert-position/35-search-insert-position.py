class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # if target <= nums[0]:
        #     return -1
        # if target >= nums[-1]:
        #     return len(nums)
        
        #wanna see magic
        n = len(nums)
        l = 0
        r = n - 1
        while l <= r:
            mid = (l + r)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return l
        #it is so gooood that BS always land left at pos where target ele should be, wow u did nothing
                